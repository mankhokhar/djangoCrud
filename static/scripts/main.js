$(document).ready( ()=>{
    $(".comment_edit_form").on('submit',edit_comment_handler)
    $(".comment_add_form").on('submit', add_comment_handler)
    $(".delete_comment").on('click', delete_comment_handler)
    $(".react_button").on('click', react_handler)
})

function edit_comment_handler(event){
    event.preventDefault();
    comment_id = parseInt(this.id.match(/[0-9]+/)[0]);
    data={'comment_id': comment_id ,
         comment_text : $(this).find('.form-control').val(),}
    serverRequestControl(this, method='POST', url='update_comment/', id=comment_id, data=data ,callback=edit_comment);
}

function add_comment_handler(event){
    event.preventDefault();
    post_id = parseInt(this.id.match(/[0-9]+/)[0]);
    data={'post_id': post_id ,
         comment_text : $(this).find('.form-control').val(),};
    serverRequestControl(this, method='POST', url='add_comment/', id=post_id, data=data ,callback=add_comment);
}

function delete_comment_handler(event){
        comment_id = parseInt($(this).parent().attr('id').match(/[0-9]+/)[0]);
        serverRequestControl(this,method='GET',url='/delete_comment/',
                              id=comment_id, data={'comment_id': comment_id}, callback= delete_comment)
}

function react_handler(event){
    post_id = parseInt($(this).parents('.post').attr('id').match(/[0-9]+/)[0]);
    serverRequestControl(this,method='GET',url='/react/',
                              id=post_id, data={'post_id': post_id}, callback= react)
}

function edit_comment(comment_id, json){
    $(`#comment_${comment_id}_text`).text(json.comment_text);
    $(`#comment_${comment_id}` + ' #hideShow').attr('aria-expanded','false');
    $(`#comment_${comment_id}` + ' .collapse').toggleClass('show');
}

function add_comment(post_id, json){
    comment_id = json.comment_id
    html = `<li id="comment_${comment_id}" class="list-group-item"> <div id="comment_${comment_id}_text"> ${json.comment_text} </div>
                        <button class="btn btn-danger delete_comment">Delete</button>
                        <button class="btn btn-primary" id="hideShow" type="button" data-toggle="collapse" data-target="#commentEditForm${comment_id}" aria-expanded="false" aria-controls="commentEdit${comment_id}">
                        Edit
                        </button>
                        <div class="collapse" id="commentEditForm${comment_id}">
                            <form method="post" class="comment_edit_form" id="commentEdit${comment_id}" action="/update_comment/">
                                <input type="hidden" name="csrfmiddlewaretoken" value="${Cookies.get('csrftoken')}"/>
                                <input type="text" name="comment_text" class="form-control" placeholder="Comment Here" required id="id_comment_text">
                                <button type="submit" class="btn btn-success">Update</button>
                            </form>
                        </div>
                    </li>`
    $(`#Post${post_id} .list-group`).append(html);
    $(`#comment_${comment_id} .delete_comment`).on('click', delete_comment_handler)
    $(`#comment_${comment_id} .comment_edit_form`).on('submit', edit_comment_handler)
}

function delete_comment(comment_id,json){
    $(`#comment_${comment_id}`).remove();
}

function react(post_id, json){
    $(`#Post${post_id} .num_reacts`).text(json.reacts)
}

function serverRequestControl(element, method, url, id, data ,callback){
    if (method=='POST'){
    csrftoken = {'csrfmiddlewaretoken': $(element).find('[name=csrfmiddlewaretoken]').val()}
    data = Object.assign({}, csrftoken, data);
    }
    $.ajax({
        url : url,
        type : method,
        data : data,
        success: function(json){
            if (method=='POST'){
                $(element).find('.form-control').val('');
                }
            callback(id,json);
        },
        error : function(xhr,errmsg,err) {
            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
}

