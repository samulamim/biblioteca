from django.contrib import admin
from .models import Cidade, Autor, Editora, Leitor, Genero, Livro

class LivroInline(admin.TabularInline):
    model = Livro
    extra = 1

class AutorAdmin(admin.ModelAdmin):
    list_display = ['nome']
    search_fields = ['nome']
    inlines = [LivroInline]

# Registro dos modelos no admin
admin.site.register(Cidade)
admin.site.register(Autor, AutorAdmin)
admin.site.register(Editora)
admin.site.register(Leitor)
admin.site.register(Genero)
admin.site.register(Livro)
