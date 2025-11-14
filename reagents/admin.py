from django.contrib import admin
from .models import Reagents, ExpiringSoonFilter


@admin.register(Reagents)
class ReagentsAdmin(admin.ModelAdmin):
    list_display = ('name', 'mark', 'quantity', 'unity', 'expiration_date', 'local', 'rack', 'sector', 'users', 'verify')
    list_filter = (ExpiringSoonFilter, 'mark', 'unity', 'sector', 'local')
    search_fields = ('name', 'mark', 'local', 'sector')
    list_editable = ('quantity', 'local', 'rack')
    date_hierarchy = 'expiration_date'
    readonly_fields = ('verify',)
    
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('name', 'mark', 'quantity', 'unity')
        }),
        ('Localização', {
            'fields': ('local', 'rack', 'sector')
        }),
        ('Validade e Controle', {
            'fields': ('expiration_date', 'users', 'verify')
        }),
    )
