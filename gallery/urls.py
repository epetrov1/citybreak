from django.urls import path, include
from .views import GalleryView
from . import views

urlpatterns = [
    path('', GalleryView.as_view(), name="portfolio"),
    path('<int:pk>/', views.slide_show_view, name="detail-slug"),  
]