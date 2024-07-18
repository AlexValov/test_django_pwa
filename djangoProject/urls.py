from django.contrib import admin
from django.urls import path, include

from test_pwa import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pwa.urls')),
    path('', views.test_pwa, name='test_pwa'),
]
