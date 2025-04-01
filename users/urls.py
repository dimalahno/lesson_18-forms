from django.urls import path
from users.views import home, register

app_name = 'users'

# Список товаров
urlpatterns = [
    path("", home, name="home"),
    path("register/", register, name="register"),
]