from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect

from .models import Post
# Create your views here.


def post_list_view(request):
    posts = Post.objects.order_by('-pub_date')
    return render(request, 'posts/post_list.html', context={'posts_list': posts})


