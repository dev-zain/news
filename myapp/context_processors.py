from django.conf import settings
from .models import News,Category

def categories(request):
    return {
        'categories' : Category.objects.all()
    }

def news(request):
    return {
        'news' : News.objects.all()
    }