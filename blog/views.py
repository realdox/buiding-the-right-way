from django.shortcuts import render

from .models import Post
from django.views.generic import (
    ListView,
    DetailView,
)

class MainView(ListView):
    model = Post
    template_name = 'blog/home.html'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
