from django.contrib import admin
from .models import Hits

# Register your models here.
@admin.register(Hits)
class HitsAdmin(admin.ModelAdmin):
    name = 'Hits'
