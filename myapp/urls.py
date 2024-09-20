from django.urls import path 
from . import views 
from django.conf import settings 
from django.conf.urls.static import static 

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('registration/', views.registration, name='registration'),
    path('contact/', views.contact, name='contact'),
    path('sign_up/', views.team, name='sign_up'),
    path('single_team/<int:pk>', views.display_single_team, name='single_team'),
    path('add_player/', views.add_players, name='add_player'),
    path('team/', views.add_team, name='team'),
    path('user/', views.add_user, name='add_user'),
    path('waiver/', views.waiver, name='waiver'),
]