from django.shortcuts import render, get_object_or_404
from .models import Article

def home(request):
    return render(request, 'blog/home.html')

def articles_list(request):
    articles = Article.objects.all().order_by('-published_at')
    return render(request, 'blog/articles.html', {'articles': articles})

def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    return render(request, 'blog/article_detail.html', {'article': article})
