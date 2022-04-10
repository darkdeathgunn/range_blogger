from unicodedata import name
from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('login/', login_view, name='login_view'),
    path('register', register_view, name='register_view'),
    path('logout/',logout_view,name='logout_view'),
    path('add-blog/',add_blog,name='add_blog'),
    path('see-blog/<slug>',see_blog,name='see_blog'),
    path('blog_list/',blog_list,name='blog_list'),
    path('blog_update/<slug>',blog_update,name='blog_update'),
    path('image_update/<slug>',image_update,name='image_update'),
    path('blog_delete/<id>',blog_delete,name='blog_delete'),
]
