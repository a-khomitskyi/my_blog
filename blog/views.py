from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.views.generic import ListView, DetailView
from django.db.models import F
from django.conf import settings

from .models import Category, Post, Project
from .forms import ContactForm
import os


def index(request):
    return render(request, 'blog/index.html')


class ViewAllPosts(ListView):
    model = Post
    template_name = 'blog/main-blog.html'
    context_object_name = 'posts'
    paginate_by = 8
    allow_empty = False

    def get_queryset(self):
        return Post.objects.all().select_related()


class ViewCategoryPost(ListView):
    template_name = 'blog/category_posts.html'
    context_object_name = 'posts'
    paginate_by = 4
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.get(slug=self.kwargs['slug'])
        return context

    def get_queryset(self):
        return Post.objects.filter(category_id__slug=self.kwargs['slug']).select_related()


class ViewPost(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'blog/post.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        Post.objects.filter(slug=self.kwargs['slug']).update(views=F('views') + 1)
        return context

    def get_queryset(self):
        return Post.objects.filter(slug=self.kwargs['slug']).select_related()


def about(request):
    return render(request, 'blog/about.html')


class ViewProjects(ListView):
    template_name = 'blog/view_projects.html'
    model = Project
    context_object_name = 'projects'
    paginate_by = 8
    allow_empty = False


class ViewProject(DetailView):
    template_name = 'blog/view_project.html'
    context_object_name = 'project'
    model = Project

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        Project.objects.filter(slug=self.kwargs['slug']).update(views=F('views') + 1)
        return context

    def get_queryset(self):
        return Project.objects.filter(slug=self.kwargs['slug'])


class ViewTagProjects(ListView):
    template_name = 'blog/tag_projects.html'
    model = Project
    context_object_name = 'projects'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # Shit I know...
        context['tag'] = str(self.request.path).split('/')[-1]
        return context

    def get_queryset(self):
        return Project.objects.filter(technology_id__slug=self.kwargs['slug'])


def view_send_mail(request):
    if request.method == 'POST':
        form = ContactForm(data=request.POST)
        if form.is_valid():
            res = send_mail(subject=form.cleaned_data['email'], message=form.cleaned_data['message'],
                            from_email=os.environ['EMAIL_HOST'], recipient_list=[os.environ['EMAIL_RECIPIENT'], ])
            letter = open('email_confirmation.txt').read()
            repl = send_mail('Mail confirmation', str(letter), os.environ['EMAIL_HOST'], [form.cleaned_data['email']])
            if res and repl:
                messages.success(request, 'Message has been sent')
                print(res)
                print(request.POST)
                return redirect('home')
            else:
                messages.error(request, 'Something wrong... Please, repeat later')
                return redirect('home')
    else:
        form = ContactForm()
    return render(request, 'blog/contact.html', {'form': form})
