# -*- coding: utf-8 -*-

from django.contrib import admin

from django.db import models

from django.contrib.auth.models import User  # Import the User model

from django.utils import timezone

from datetime import timedelta

        

class Reagents(models.Model):

    UNITY_CHOICES = [

        ('g', 'g'),

        ('mL', 'mL'),

        ('kit', 'kit'),

        ('kg', 'kg'),

        ('un.', 'un.'),

    ]

    

    name = models.CharField(max_length=255, verbose_name="Nome do Reagente")

    mark = models.CharField(max_length=50, verbose_name="Marca")

    quantity = models.IntegerField(verbose_name="Quantidade", default=0)

    unity = models.CharField(max_length=10, choices=UNITY_CHOICES, null=True, blank=True, verbose_name="Unidade")

    expiration_date = models.DateField(null=True, blank=True, verbose_name="Data de Validade")

    local = models.CharField( max_length=50, default="-", verbose_name="Localizacao")

    rack = models.CharField(max_length=50, blank=True, verbose_name="Prateleira")

    verify = models.DateTimeField(auto_now=True,  verbose_name="Verificacao")

    users = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, verbose_name='Usuario')

    sector = models.CharField(max_length=50, blank=True, default="-", verbose_name="Setor")

    

       

  

    class Meta:

        ordering = ['name']

        verbose_name = "Reagente"

    def __str__(self):

        return self.name

class ExpiringSoonFilter(admin.SimpleListFilter):

    title = 'Vencimento'

    parameter_name = 'expiring_soon'

    def lookups(self, request, model_admin):

        return (

            ('yes', '30 dias'),

        )

    def queryset(self, request, queryset):

        if self.value() == 'yes':

            now = timezone.now().date()

            return queryset.filter(expiration_date__lte=now + timedelta(days=30))

        return queryset
