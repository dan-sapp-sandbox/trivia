from django.contrib import admin
from .models import Element

@admin.register(Element)
class ElementAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'number', 'symbol')
