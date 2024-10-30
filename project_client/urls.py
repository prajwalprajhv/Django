from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('management.urls')),         # Main interface
    path('api/', include('management.api_urls')),  # API endpoints
]
