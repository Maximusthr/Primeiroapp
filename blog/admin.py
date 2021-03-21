from django.contrib import admin

from .models import Post, Enxadrista, JogadoresFavorito

# Register your models here.

admin.site.register(Post)
admin.site.register(JogadoresFavorito)

@admin.register(Enxadrista)
class EnxadristaAdmin(admin.ModelAdmin):
    list_display = (
        "nome", 
        "titulo", 
        "pais", 
        "idade"
    )