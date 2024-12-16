from django.contrib import admin
from django.urls import path,  include
import user.views
import trainer.views
import booking.views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("user/", include("user.urls")),

    path("booking/", include("booking.urls")),

    path("trainer/", include("trainer.urls")),
    path("login/", user.views.login_page,  name="user_login"),
    path("logout/", user.views.logout_page, name="uesr_logout"),
    path("register/", user.views.register_page, name="user_register")
]