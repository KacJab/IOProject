from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('gamemode/', views.gamemode, name='gamemode'),
    path('game/<mode>/', views.game, name='game'),
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('login_player2/', views.login_player2, name='login_player2'),
    path('logout/', views.logoutUser, name='logout'),
    path('statistics/', views.statistics, name='statistics'),
    path('playerpanel/', views.playerpanel, name='playerpanel'),
    path('password_change/', views.password_change, name='password_change'),
    path('delete_account/', views.delete_account, name='delete_account'),
    path('saveresult/<mode>/', views.save_result, name='saveresult'),
    path('allgames/', views.allgames, name='allgames'),
    path('replay/<result_id>', views.replay, name='replay')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)