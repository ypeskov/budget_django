from django.urls import path, include

from . import views

app_name = 'profiles'
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('', views.home_page, name='home_page'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register')
]
