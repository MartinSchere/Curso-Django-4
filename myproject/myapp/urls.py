from django.urls import path

from .views import ListaDeAutos, AutoDetail

urlpatterns = [
    path('', ListaDeAutos.as_view(), name="index"),
    path('<int:pk>', AutoDetail.as_view(), name="auto_detail"),
]
