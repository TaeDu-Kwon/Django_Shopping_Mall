from django.urls import path

from . import views
from django.contrib.auth import views as auth_views

app_name = "user"

urlpatterns = [
    path("",auth_views.LoginView.as_view(template_name = "users/init_page.html"), name = "login"),
    path('logout/', views.logout_view, name='logout'),
    path("signup/",views.signup, name = "signup"),
]