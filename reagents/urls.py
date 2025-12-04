from django.urls import path
from . import views

app_name = 'reagents'

urlpatterns = [
    path('report/', views.reagents_report, name='reagents_report'),
]


