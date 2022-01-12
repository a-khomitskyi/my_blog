from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.core.mail import send_mail
from django.contrib import messages
from django.db.models import Count

from .models import Category, Post, Project, Technology
from .forms import ContactForm
import os


class HomeBlog(ListView):
    template_name = 'blog/index.html'


def index(request):
    posts = Post.objects.all().select_related()
    recent_posts = posts.order_by('-created_at')[:4]
    most_pop_posts = posts.order_by('-views')[:4]
    recent_projects = Project.objects.all().order_by('-id')[:4]
    most_used_technologies = Project.objects.annotate(cnt=Count('technology_id__name')).order_by('-cnt')
    print(most_used_technologies)
    return render(request, 'blog/index.html', {'recent_posts': recent_posts, 'most_pop_posts': most_pop_posts,
                                               'recent_projects': recent_projects, 'most_used_technologies': most_used_technologies})


def get_all_posts(request):
    posts = Post.objects.all()
    return render(request, 'blog/main-blog.html', {'posts': posts})


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
    projects = Project.objects.all().order_by('-id')
    return render(request, 'blog/view_projects.html', {'projects': projects})


def get_project(request, slug):
    project = Project.objects.get(slug=slug)
    return render(request, 'blog/view_project.html', {'project': project})


def view_send_mail(request):
    if request.method == 'POST':
        form = ContactForm(data=request.POST)
        if form.is_valid():
            res = send_mail(subject=form.cleaned_data['email'], message=form.cleaned_data['message'],
                            from_email=os.environ['EMAIL_HOST'], recipient_list=[os.environ['EMAIL_RECIPIENT'], ])
            if res:
                messages.success(request, 'Message has been sending')
                print(res)
                print(request.POST)
                return redirect('home')
            else:
                messages.error(request, 'Something wrong... Please, repeat later')
                return redirect('home')
    else:
        form = ContactForm()
    return render(request, 'blog/contact.html', {'form': form})
