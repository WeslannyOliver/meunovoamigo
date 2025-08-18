# pets/admin.py
from django.contrib import admin
from .models import Pet

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'idade')  # colunas visíveis no admin
