from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('detail/<str:slug>',views.detail,name='detail'),
    path('category/<str:slug>',views.category,name='category'),
]