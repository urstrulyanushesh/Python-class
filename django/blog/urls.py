from django.urls import path
from .views import Home, Category, Blog, Single, Contact

urlpatterns = [
    path('',Home,name="index"),
    path('category',Category,name="category"),
    path('blog',Blog,name="indeblog"),
    path('single',Single,name="single"),
    path('contact',Contact,name="contact"),
]
