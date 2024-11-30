from django.contrib import admin
from .models import Pokemon

@admin.register(Pokemon)
class SongAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'types', 'gen_of_first_appearance')