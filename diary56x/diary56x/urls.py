from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", TemplateView.as_view(template_name="index.html"), name="index"),
    path("api/private/auth/users/", include("apps.authentication.urls")),
    path(
        "api/private/auth/token/",
        TokenObtainPairView.as_view(),
        name="token_obtain_pair",
    ),
    path(
        "api/private/auth/token/refresh/",
        TokenRefreshView.as_view(),
        name="token_refresh",
    ),
]
