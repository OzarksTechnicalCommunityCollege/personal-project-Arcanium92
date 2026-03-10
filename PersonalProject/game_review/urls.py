from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("review/", views.review_list, name="review_list"),
    path("add/", views.add_review, name="add_review"),
    path("result/<int:pk>/", views.review_result, name="review_result"),
    path("register/", views.register, name="register"),
    path("registration/", views.logged_out, name="logged_out"),
    path("like/<int:review_id>/", views.toggle_like, name="toggle_like"),
]