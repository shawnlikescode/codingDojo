from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("register", views.register, name="register"),
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout"),
    path("wish_items/create", views.createitem, name="create"),
    path("additem", views.additem, name="additem"),
]
