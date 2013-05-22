# Create your views here.
from django.shortcuts import render
from businessPortfolioNews.models import NewsArticle
def index(request):
    articles_list = NewsArticle.objects.order_by('-pubdate')
    return render(request, 'businessPortfolioNews/news.html', {'articles_list': articles_list})