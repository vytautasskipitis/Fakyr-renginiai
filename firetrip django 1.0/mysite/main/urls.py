from django.urls import path

from . import views

# Reikia Auth middleware arba router blocking
urlpatterns = [
  path("<int:id>", views.index, name="index"),
  path("", views.home, name="home"),
  path("home_login/", views.home_login, name="home_login"),

  path("vip/", views.vip, name="vip"),
  path("galerija/", views.galerija, name="galerija"),
  path("pasirodymai/", views.pasirodymai, name="pasirodymai"),
  path("apie_mus/", views.apie_mus, name="apie_mus"),

  path("duombaze/", views.duombaze, name="duombaze"),
  path("vip_kalendorius/", views.vip_kalendorius, name="vip_kalendorius"),
  path("iranga/", views.iranga, name="iranga"),

]

