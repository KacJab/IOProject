from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('gamemode/', views.gamemode, name='gamemode'),
    path('game/<mode>/', views.game, name='game'),
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    # path('game/', views.gameWithOtherPlayer, name='gWOP' ),

]