import json

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.template.loader import render_to_string
from django.middleware.csrf import get_token


from .models import Post, Comment
from .forms import CommentForm
# Create your views here.


def post_list_view(request):
    posts = Post.objects.order_by('-pub_date')
    comment_form = CommentForm()
    return render(request, 'posts/post_list.html', context={'posts_list': posts, 'comment_form': comment_form})


def react(request):
    post_id = request.GET['post_id']
    post = get_object_or_404(Post, pk=post_id)
    post.reacts += 1
    post.save()
    return HttpResponse(
        json.dumps({'reacts': post.reacts}),
        content_type='application/json'
    )


def search_post(request):
    query_parameter = request.GET['q']
    posts = Post.objects.filter(title__icontains=query_parameter).order_by('-pub_date')
    html = render_to_string('posts/post.html', {'posts_list': posts, 'comment_form': CommentForm, 'csrf_token': get_token(request)})
    return HttpResponse(html)


def add_comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            post_id = request.POST['post_id']
            post = get_object_or_404(Post, pk=post_id)
            comment = post.comment_set.create(comment_text=request.POST['comment_text'])
            html = render_to_string('posts/comment.html',
                                    {'comment': comment , 'csrf_token': get_token(request), 'comment_form': CommentForm})
            return HttpResponse(
                json.dumps({'comment_id': comment.id, 'html_view': html}),
                content_type='application/json'
            )
    else:
        form = CommentForm()
    return HttpResponseRedirect('/')


def update_comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment_id = request.POST['comment_id']
            comment = get_object_or_404(Comment, pk=comment_id)
            comment.comment_text = request.POST['comment_text']
            comment.save()
            return HttpResponse(
                json.dumps(form.cleaned_data),
                content_type='application/json'
            )
    else:
        form = CommentForm()
    return HttpResponseRedirect('/')


def delete_comment(request):
    comment_id = request.GET['comment_id']
    comment = get_object_or_404(Comment, pk=comment_id)
    comment.delete()
    return HttpResponse()
