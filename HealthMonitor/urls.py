from django.contrib import admin
from django.urls import path
from HealthMonitor import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('',views.index,name='index'),
    path('HandleLogin',views.HandleLogin,name='login'),
    path('HandleLogout',views.HandleLogout,name='logout'),
    path('Register',views.Register,name='Register'),
    path('storesymptoms',views.storesymptoms,name='storesymptoms'),
    path('table',views.Table,name='table'),
    path('team',views.team,name='team'),
] 
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)