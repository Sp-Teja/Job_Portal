from django.urls import path
from.views import *

urlpatterns=[
    # path("register/", register),
    # path("login/", login),

    # # UI Pages
    # path("login/page/", login_page, name="login_page"),
    # path("register/page/", register_page, name="register_page"),

    # # API Endpoints
    # path("register/", register, name="register_api"),
    # path("login/", login, name="login_api"),
]

urlpatterns = [
    path("register/", register, name="register_api"),
    path("login/", login, name="login_api"),
    path("login/page/", login_page, name="login_page"),
    path("register/page/", register_page, name="register_page"),
]
