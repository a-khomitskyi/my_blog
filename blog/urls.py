from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('blog/', ViewAllPosts.as_view(), name='all_posts'),
    # path('blog/', get_all_posts, name='all_posts'),
    path('category/<str:slug>', ViewCategoryPost.as_view(), name='category'),
    # path('category/<str:slug>', get_category_posts, name='category'),
    path('post/<str:slug>', ViewPost.as_view(), name='post'),
    # path('post/<str:slug>', get_post, name='post'),
    path('about', about, name='about'),
    path('projects/', ViewProjects.as_view(), name='projects'),
    # path('projects/', get_list_project, name='projects'),
    path('pet/<str:slug>', ViewProject.as_view(), name='project'),
    # path('pet/<str:slug>', get_project, name='project'),
    path('contact/', view_send_mail, name='contact'),
    path('tag/<str:slug>', ViewTagProjects.as_view(), name='tag_projects'),
]
