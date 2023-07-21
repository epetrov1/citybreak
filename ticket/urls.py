from django.urls import path, include
from . import views
from . views import CreateCheckoutSessionView

urlpatterns = [
    path('success/', views.success_view, name="success-page"),
    path('cancel/', views.failed_view, name="failed-page"),
    path('create-checkout-session/', CreateCheckoutSessionView.as_view(), name="create-checkout-session"),
    path('webhook-stripe/', views.stripe_webhook_view, name="webhook-stripe"),
]