from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('tournaments/', views.tournamentPage.as_view(), name='tournament'),
    path('races/', views.racePage.as_view(), name='race'),
    path('fractions/', views.fractionPage.as_view(), name='fraction'),
    path('game worlds/', views.gameWorldPage.as_view(), name='game_world'),
    path('download/', views.downloadPage.as_view(), name='download'),
    path('allience/', views.allienceDetailPage.as_view(), name='allience_detail'),
    path('horde/', views.hordeDetailPage.as_view(), name='horde_detail'),
    path('renegades/', views.renegadesDetailPage.as_view(), name='renegades_detail'),
]