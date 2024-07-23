from django.urls import path
from menu import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('about/team/', views.team, name='team'),
    path('about/history/', views.history, name='history'),
    path('contact/', views.contact, name='contact'),
]
