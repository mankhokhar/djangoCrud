from django.shortcuts import render, get_object_or_404


from .models import Post
# Create your views here.


def post_list_view(request):
    posts = Post.objects.order_by('-pub_date')
    return render(request, 'posts/post_list.html', context={'posts_list': posts})


def react(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.reacts += 1
    post.save()
    return post_list_view(request)


def add_comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.comment_set.create(comment_text=request.POST['comment_text'])
    return post_list_view(request)
