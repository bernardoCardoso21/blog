from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('articles/', views.articles_list, name='articles'),
    path('articles/<slug:slug>/', views.article_detail, name='article_detail'),
]
