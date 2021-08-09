function deleteComment(comment_id){
    let confirmation = confirm("Delete this comment?")
    if (confirmation) {
        window.location.replace(`/${comment_id}/delete`);
    }
}

$(document).ready( ()=>{
    attachFunc2Forms()
})

function attachFunc2Forms(){
    $(".comment_edit_form").on('submit', function(event){
    event.preventDefault();
    comment_id = parseInt(this.id.match(/[0-9]+/)[0]);
    data={'comment_id': comment_id ,
         comment_text : $(this).find('.form-control').val(),}
    formPostControl(this, 'update_comment/', id=comment_id, data=data ,callback=edit_comment);
    });

    $(".comment_add_form").on('submit', function(event){
    event.preventDefault();
    post_id = parseInt(this.id.match(/[0-9]+/)[0]);
    data={'post_id': post_id ,
         comment_text : $(this).find('.form-control').val(),};
    formPostControl(this, 'add_comment/', id=post_id, data=data ,callback=add_comment);
    });
}

function edit_comment(comment_id, json){
    $(`#comment_${comment_id}_text`).text(json.comment_text);
    $(`#comment_${comment_id}` + ' #hideShow').attr('aria-expanded','false');
    $(`#comment_${comment_id}` + ' .collapse').toggleClass('show');
}

function add_comment(post_id, json){
    comment_id = json.comment_id
    html = `<li id="comment_${comment_id}" class="list-group-item"> <div id="comment_${comment_id}_text"> ${json.comment_text} </div>
                        <button class="btn btn-danger" onclick="deleteComment(${comment_id})">Delete</button>
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
    attachFunc2Forms();
}


function formPostControl(element, url, id, data ,callback){
    csrftoken = {'csrfmiddlewaretoken': $(element).find('[name=csrfmiddlewaretoken]').val()}
    data = Object.assign({}, csrftoken, data);
    $.ajax({
        url : url,
        type : 'POST',
        data : data,
        success: function(json){
            $(element).find('.form-control').val('');
            callback(id,json);
        },
        error : function(xhr,errmsg,err) {
            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
}

