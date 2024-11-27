from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('start/', views.start_game, name='start_game'),
    path('game/', views.play_game, name='play_game'),
    path('game-over/', views.game_over, name='game_over'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
    path('notebooks/<str:notebook_name>/', views.view_notebook, name='view_notebook'),
]
if True:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)