from django.shortcuts import render, get_object_or_404
from .models import Post
from django.http import Http404

# Create your views here.

#return a list of all published posts using custom models manager, published
def post_list(request):
    posts = Post.published.all()
    return render(request, 'blog/post/list.html', {'posts': posts})

#returns a single post if it exist otherwise return error 404
def post_detail(request, id):
    post = get_object_or_404(Post, id=id, status=Post.Status.PUBLISHED)
    return render(request, 'blog/post/detail.html', {'post': post})