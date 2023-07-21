from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home_view, name='home-page'),  
    path('cookie-consent', views.cookie_consent, name='cookie_consent'),
    path('cookie-description', views.cookie_description, name='cookie_description'),
]