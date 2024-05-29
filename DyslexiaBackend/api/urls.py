from django.urls import path
from .views import GetWords

urlpatterns = [
    # Example URL pattern
    path('v1/', GetWords.as_view(), name='GetWords'),
    # Add more URL patterns as needed
]
