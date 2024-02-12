from . import views
from django.urls import path


app_name = 'accounts'
urlpatterns = [
    path("", views.index, name="index"),
    # login
    path("login/", views.login_view, name="login_view"),
    # logout
    path("logout/", views.logout_view, name="logout_view"),
    # registration/signup
    path("signup/", views.signup_view, name="signup_view"),
]