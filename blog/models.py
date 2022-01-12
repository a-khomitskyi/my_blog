from django.db import models
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=120, verbose_name='Title')
    slug = models.SlugField(max_length=120, verbose_name='URL', unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['id', ]


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='Title')
    content = models.TextField(verbose_name='Content')
    slug = models.SlugField(max_length=255, verbose_name='URL', unique=True)
    created_at = models.DateTimeField(verbose_name='Created at', auto_now_add=True)
    photo = models.ImageField(verbose_name='Photo', upload_to='media/%Y/%m/%d/', blank=True)
    views = models.IntegerField(default=0, verbose_name='Views')
    category_id = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Category', related_name='posts')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['-created_at', 'title', ]


class Project(models.Model):
    title = models.CharField(max_length=255, verbose_name='Title')
    content = models.TextField(verbose_name='Content')
    photo = models.ImageField(upload_to='media/%Y/%m/%d/', verbose_name='Photo', blank=True)
    slug = models.SlugField(max_length=255, unique=True, verbose_name='URL')
    views = models.IntegerField(default=0, verbose_name='Views')
    technology_id = models.ManyToManyField('Technology', verbose_name='Technology')

    def get_absolute_url(self):
        return reverse('project', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
        ordering = ['id', ]


class Technology(models.Model):
    name = models.CharField(max_length=60, verbose_name='Title')
    slug = models.SlugField(max_length=60, unique=True, verbose_name='URL')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Technology'
        verbose_name_plural = 'Technologies'
        ordering = ['name', ]
