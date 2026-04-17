from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from cars.views import CarsListView, newCarCreateView
from accounts.views import register_view, login_view, logout_view


urlpatterns = [
    path("admin/", admin.site.urls),
    path("register/", register_view, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("cars/", CarsListView.as_view(), name="cars_list"),
    path("new_car/", newCarCreateView.as_view(), name="new_car"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # Adiciona as URLs para servir arquivos de mídia durante o desenvolvimento, usando as configurações MEDIA_URL e MEDIA_ROOT do settings.py
