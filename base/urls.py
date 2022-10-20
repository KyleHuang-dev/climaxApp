from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('climax/<str:pk>', views.climax, name = "climax"),

    path('createClimax', views.createClimax, name = "createClimax"),
    path('updateClimax/<str:pk>', views.updateClimax, name = "updateClimax"),
    path('deleteClimax/<str:pk>', views.deleteClimax, name = "deleteClimax"),
]