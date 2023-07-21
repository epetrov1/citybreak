from django.shortcuts import render
from django.views.generic import ListView
from .models import Faq

class FaqView(ListView):
    model = Faq
