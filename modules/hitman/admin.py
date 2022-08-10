from django.contrib import admin
from .models import Hitmen

# Register your models here.
@admin.register(Hitmen)
class HitmanAdmin(admin.ModelAdmin):
    name = 'Hitmen'
