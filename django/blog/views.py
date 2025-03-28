from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request,"index.html")

def Category(request):
    return render(request, "category.html")

def Blog(request):
    return render(request, "blog.html")

def Single(request):
    return render(request, "single.html")

def Contact(request):
    return render(request, "contact.html")