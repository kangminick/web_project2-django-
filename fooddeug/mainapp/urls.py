from django.urls import path
from . import views
urlpatterns = [
    path('main/', views.main, name='main'),
    path('join/', views.join, name='join'),
    path('login/', views.login, name='login'),
    path('swipe/', views.swipe, name='swipe'),
    path('mypage/', views.mypage, name='mypage'),
    path('detail/', views.detail, name='detail'),
    path('like/', views.like, name='like'),
]
