from django.conf import settings
from django.conf.urls.static import static
from django.urls import path


from .views import *


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('blog/', get_all_posts, name='all_posts'),
    path('category/<str:slug>', get_category_posts, name='category'),
    path('post/<str:slug>', get_post, name='post'),
    path('about', about, name='about'),
    path('projects/', get_list_project, name='projects'),
    path('pet/<str:slug>', get_project, name='project'),
    path('contact/', view_send_mail, name='contact'),
]
