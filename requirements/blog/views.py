from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Blog
# Create your views here.
def Home(request):
    blog = Blog.objects.all()
    category = Category.objects.all()
    context = {
        'blog' : blog,
        'category': category
    }
    print(blog)
    return render(request, "index.html",context)

def Categorys(request, pk):
    category = get_object_or_404(Category, id = pk)
    blog = Blog.objects.filter(category = category)
    return render(request, "category.html", 
                  {'blog': blog})

def Blogs(request):
    blog = Blog.objects.all()
    return render(request, "blog.html", {'blog': blog})

def Single(request, pk):
    singleblog = get_object_or_404(Blog, id= pk)
    return render(request, "single.html", {'singleblog': singleblog})

def Contact(request):
    return render(request, "contact.html")