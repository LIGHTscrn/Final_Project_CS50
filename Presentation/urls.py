from django.urls import path
from . import views

app_name = 'presentation'

urlpatterns = [
    path('', views.home, name='home'),
    path('demo/', views.demo, name='demo'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
