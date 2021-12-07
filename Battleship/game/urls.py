from django.urls import path
from . import views

urlpatterns = [
    path('game/', views.game, name='game'),
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
]