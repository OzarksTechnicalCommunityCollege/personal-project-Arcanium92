from django.urls import path
from . import views

urlpatterns = [
    path('', views.chart_page, name='chart_page'),
    path('data-bar/', views.ratings_by_game_title, name='bar-chart'),
    path('data-pie/', views.ratings_by_game_title, name='pie-chart'),
]
