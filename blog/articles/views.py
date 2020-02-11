from django.shortcuts import render
from .models import Article
from django.views.generic import ListView, DetailView


class ArticleListView(ListView):
    model = Article
    template_name = 'home.html'
    context_object_name = "articles"


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'detail.html'
