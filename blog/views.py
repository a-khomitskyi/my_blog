from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.http import HttpResponse

from .models import Category, Post


class HomeBlog(ListView):
    template_name = 'blog/index.html'


def index(request):
    return render(request, 'blog/index.html')


def get_category(request, slug):
    category = Category.objects.get(slug=slug)
    posts = Post.objects.filter(category_id__slug=slug)
    return render(request, 'blog/category_posts.html', {'category': category, 'posts': posts})


def get_post(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'blog/post.html', {'post': post})


def about(request):
    return render(request, 'blog/about.html')


def get_list_project(request):
    return render(request, 'blog/view_projects.html')


def get_project(request, slug):
    return render(request, 'blog/view_project.html')
