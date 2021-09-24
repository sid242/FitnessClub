from django.contrib import admin
from django.urls import path
from home import views


urlpatterns = [
    path("", views.index, name='home'),
    path("class.html", views.classes, name='classes'),
    path("about.html", views.about, name='about'),
    path("contact.html", views.contact, name='contact'),
    path("signup", views.handleSignUp, name='handleSignUp'),
    path('login', views.handeLogin, name="handleLogin"),
    path('logout', views.handelLogout, name="handleLogout"),
]
