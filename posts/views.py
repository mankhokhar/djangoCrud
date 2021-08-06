from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect


from .models import Post, Comment
from .forms import CommentForm
# Create your views here.


def post_list_view(request):
    posts = Post.objects.order_by('-pub_date')
    comment_form = CommentForm()
    return render(request, 'posts/post_list.html', context={'posts_list': posts, 'comment_form': comment_form})


def react(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.reacts += 1
    post.save()
    return HttpResponseRedirect('/')


def add_comment(request, post_id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            post = get_object_or_404(Post, pk=post_id)
            post.comment_set.create(comment_text=request.POST['comment_text'])
            return HttpResponseRedirect('/')
    else:
        form = CommentForm()
    return HttpResponseRedirect('/')


def delete(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    comment.delete()
    return HttpResponseRedirect('/')


def update_comment(request, comment_id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = get_object_or_404(Comment, pk=comment_id)
            comment.comment_text = request.POST['comment_text']
            comment.save()
            return HttpResponseRedirect('/')
    else:
        form = CommentForm()
    return HttpResponseRedirect('/')
