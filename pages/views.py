from django.shortcuts import render
from django.http import JsonResponse



def home_view(request):
    return render(request, 'pages/home.html')


def cookie_consent(request):
    return render(request, 'pages/cookie_consent.html')

def cookie_description(request):
    return render(request, 'pages/cookie_policy.html')