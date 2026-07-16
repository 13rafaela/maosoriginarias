from django.urls import include, path
from . import views

app_name = "maos_originarias"

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.login, name="login"),
    path("produto/", views.produto, name="produto"),
    path("artesas/", views.artesas, name="artesas")
   
]