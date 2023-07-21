from django.shortcuts import render
from . models import BlogPost
from django.views.generic import ListView, DetailView

class BlogDetailView(DetailView):
    model = BlogPost

class BlogListView(ListView):
    model = BlogPost
    ordering = ['-date_create']