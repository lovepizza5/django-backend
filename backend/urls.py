from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),         # 👈 Add this line
    path('api/', include('formapi.urls')),   # Your API routes
]
