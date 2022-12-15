from django.urls import path
from django.contrib.auth import views as auth_views

from .views import UserRegisterView, IndexView


urlpatterns = [
    path("", IndexView.as_view(), name="Home page"),
    path("register/", UserRegisterView.as_view(), name="Registration"),
    path("login/", auth_views.LoginView.as_view(template_name="login.html"), name="Login"),
    path("logout/", auth_views.LogoutView.as_view(template_name="logout.html"), name="Logout"),
]
