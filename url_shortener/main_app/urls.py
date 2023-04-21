from django.urls import path
from .views import home, url_created, create_short_url

urlpatterns = [
    path("", home, name="home"),
    path("create_short_url", create_short_url, name="create_short_url"),
    path("url_created/", url_created, name="url_created"),
]
