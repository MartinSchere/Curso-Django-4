from django.contrib import admin

from .models import Auto, Mejora, Patente, Fabrica

admin.site.register([Auto, Mejora, Patente, Fabrica])
