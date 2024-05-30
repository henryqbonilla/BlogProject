from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post
from django.http import Http404

# Create your views here.

#return a list of all published posts using custom models manager, published
def post_list(request):
    post_list = Post.published.all()
    #Pagination with 3 posts per page #96
    paginator = Paginator(post_list, 3)
    page_number = request.GET.get('page', 1)
    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        #If page_number is not an integer get the first page
        posts = paginator.page(1)
    except EmptyPage:
        #If page_number is out of range get last page of results
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/post/list.html', {'posts': posts})

#returns a single post if it exist otherwise return error 404
def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, status=Post.Status.PUBLISHED, slug=post, publish__year=year,
                             publish__month=month,publish__day=day)
    return render(request, 'blog/post/detail.html', {'post': post})