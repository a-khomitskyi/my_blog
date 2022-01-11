from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.core.mail import send_mail
from django.contrib import messages

from .models import Category, Post
from .forms import ContactForm


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


def view_send_mail(request):
    if request.method == 'POST':
        form = ContactForm(data=request.POST)
        if form.is_valid():
            res = send_mail(subject=form.cleaned_data['email'], message=form.cleaned_data['message'],
                            from_email='twfkbpvuxtu@frederictonlawyer.com', recipient_list=['ganjuibas@gmail.com', ])
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
