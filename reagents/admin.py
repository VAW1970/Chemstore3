from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
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

    def changelist_view(self, request, extra_context=None):
        """Adiciona botão de relatório na página de lista"""
        extra_context = extra_context or {}
        extra_context['report_url'] = reverse('reagents:reagents_report')
        return super().changelist_view(request, extra_context)
