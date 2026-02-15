from django.urls import path
from . import views

#URL routing
urlpatterns = [
    path("", views.home, name="home"), #changed to make the homepage seperate from the submitted reviews.
    path("review/", views.review_list, name="review_list"),
    path("add/", views.add_review, name="add_review"),
    path("result/<int:pk>/", views.review_result, name="review_result"),
]