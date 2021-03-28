from django.urls import path

from account import views

urlpatterns = [
    path("admin-signup/", views.AdminSignUp.as_view()),
    path("signup/", views.UserSignUp.as_view()),
    path("login/", views.login),


]