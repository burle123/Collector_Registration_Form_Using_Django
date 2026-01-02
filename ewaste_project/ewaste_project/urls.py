from django.contrib import admin
from django.urls import path,include
from django.shortcuts import redirect
from collector import views


urlpatterns = [
    path('', lambda request: redirect('collector_registration')),
    path('admin/', admin.site.urls),
    path('collector/', include('collector.urls')),
    
    
]
 
