from django.urls import path, include
from .views import BlogDetailView, BlogListView
urlpatterns = [
    path('<slug:slug>/', BlogDetailView.as_view(), name="detail_blog"),
    path('', BlogListView.as_view(), name="list_blog"),
]