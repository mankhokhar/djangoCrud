from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect


from .models import Post, Comment
# Create your views here.


def post_list_view(request):
    posts = Post.objects.order_by('-pub_date')
    return render(request, 'posts/post_list.html', context={'posts_list': posts})


def react(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.reacts += 1
    post.save()
    return HttpResponseRedirect('/')


def add_comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.comment_set.create(comment_text=request.POST['comment_text'])
    return HttpResponseRedirect('/')


def delete(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    comment.delete()
    return HttpResponseRedirect('/')


def update_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    comment.comment_text = request.POST['comment_text_edit']
    comment.save()
    return HttpResponseRedirect('/')
