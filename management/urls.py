from django.urls import path, include

urlpatterns = [
    path('', include('management.api_urls')),  # API endpoints
]