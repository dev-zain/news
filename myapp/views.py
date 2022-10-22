from django.shortcuts import render
from .models import News,Category

# Create your views here.

def home(request):
    news  = News.objects.all()
    categories = Category.objects.all()
    
    context = {
        'categories' : categories,
        'news' : news,
    }
    return render (request,'myapp/home.html',context)
        


def detail(request,slug):

    new = News.objects.get(slug=slug)
    # new  = News.objects.all()
    context = {
        # 'news' : news,
        'new' : new,
    }

    return render(request,'myapp/detail.html',context)


def category(request,slug):
    categories = Category.objects.all()
    category = Category.objects.get(slug=slug)

    context = {
        'categories' : categories,
        'category' : category,
    }

    return render(request,'myapp/category.html',context)



    
