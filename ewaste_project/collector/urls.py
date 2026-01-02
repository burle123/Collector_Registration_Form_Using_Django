from django.urls import path
from . import views

urlpatterns = [
    path('registration/', views.collector_registration, name='collector_registration'),
    path('success/', views.collector_success, name='collector_success'),
    path('login/', views.collector_login, name='collector_login'),
    path('dashboard/', views.collector_dashboard, name='collector_dashboard'),
    path('logout/', views.collector_logout, name='collector_logout'),
    
]
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
