from django.shortcuts import render

from .models import Auto

from django.views.generic import ListView, DetailView


class ListaDeAutos(ListView):
    template_name = "myapp/index.html"
    model = Auto


class AutoDetail(DetailView):
    model = Auto
