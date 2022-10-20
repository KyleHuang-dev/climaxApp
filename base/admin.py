from django.contrib import admin

# Register your models here.

from .models import City, Climax

admin.site.register(City)
admin.site.register(Climax)