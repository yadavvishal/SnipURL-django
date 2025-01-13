from django.urls import path
from . import views

urlpatterns = [
    # URL pattern for the main page to shorten URLs
    path('', views.shorten_url, name='shorten_url'),
    # URL pattern to redirect based on the short code provided
    path('<str:short_code>/', views.redirect_url, name='redirect_url'),
]