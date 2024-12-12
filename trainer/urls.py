from django.contrib import admin
from django.urls import path, include

import user.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("user/", include("user.urls")),
    path("login/", user.views.login_page,  name="login"),
    path("logout/", user.views.logout_page, name="logout"),
    path("register/", user.views.register_page, name="register")
]