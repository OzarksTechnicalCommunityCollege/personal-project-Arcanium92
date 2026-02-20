from django.urls import include, path
from django.contrib.auth import views as AuthViews
from . import views

#URL routing
urlpatterns = [
    path("", views.home, name="home"), #changed to make the homepage seperate from the submitted reviews.
    path("review/", views.review_list, name="review_list"),
    path("add/", views.add_review, name="add_review"),
    path("result/<int:pk>/", views.review_result, name="review_result"),

    #Login and logout view
    path('', include('django.contrib.auth.urls')),
    path('login/', AuthViews.LoginView.as_view(), name='login'),
    path('logout/', AuthViews.LogoutView.as_view(), name='logout'),
    
    #Registration
    path('register/', views.register, name='register'),
]