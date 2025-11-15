
from django.contrib import admin
from django.urls import path,include
from django.conf import settings

urlpatterns = [
    path('', include('votes.urls')),
    path('admin/', admin.site.urls),
]


if settings.DEBUG:
    # Include django_browser_reload URLs only in DEBUG mode
    urlpatterns += [
        path("__reload__/", include("django_browser_reload.urls")),
    ]