from django.conf import settings
from django.conf.urls.static import static
from django.urls import path


from .views import *


urlpatterns = [
    path('', index, name='home'),
    path('category/<str:slug>', get_category, name='category'),
    path('post/<str:slug>', get_post, name='post'),
    path('about', about, name='about'),
    path('projects/', get_list_project, name='projects'),
    path('pet/<str:slug>', get_project, name='project'),
]
