from django.urls import path
from .views import Home, Categorys, Blogs, Single, Contact
urlpatterns = [
    path('', Home, name="index"),
    path('category/<int:pk>', Categorys, name="category"),
    path('blog', Blogs, name="blog"),
    path('single/<int:pk>', Single, name="single"),
    path('contact', Contact, name="contact"),
]