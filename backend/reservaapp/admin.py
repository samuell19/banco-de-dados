from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, EspacoEsportivo, Recurso, Agenda

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'tipo', 'nome_completo', 'cpf')
    list_filter = ('tipo',)
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('tipo', 'nome_completo', 'cpf')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('tipo', 'nome_completo', 'cpf')}),
    )

class EspacoEsportivoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cidade', 'UF', 'media_avaliacao')
    search_fields = ('nome', 'cidade')
    list_filter = ('cidade', 'UF')

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(EspacoEsportivo, EspacoEsportivoAdmin)
admin.site.register(Recurso)
admin.site.register(Agenda)    

# Register your models here.
