from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('counter', views.counter, name='counter'),
    path('register', views.register, name='register'),
    path('login',views.login, name='login'),
    path('blog',views.blog, name='blog'),
    path('contact',views.contact, name='contact'),
    path('portfolio',views.portfolio, name='portfolio'),
    path('propos',views.propos, name='propos'),
    path('services',views.services, name='services'),
    path('team',views.team, name='team'),
    path ('logout',views.logout, name='logout')
]