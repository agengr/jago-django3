from django.shortcuts import render
from django.views.generic import ListView, DetailView
from . models import Post

# Create your views here.
class WebBlogListView(ListView):
    model = Post
    template_name='beranda.html'

class WebBlogDetailView(DetailView):
    model = Post
    template_name='post_detail.html'