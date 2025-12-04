from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Reagents
from datetime import date, timedelta

@login_required
def reagents_report(request):
    """View para gerar relatório de reagentes com visual elegante"""
    # Obtém todos os reagentes
    reagents = Reagents.objects.all().order_by('name')

    # Estatísticas básicas
    today = date.today()
    thirty_days_from_now = today + timedelta(days=30)

    total_reagents = reagents.count()
    expiring_soon = reagents.filter(
        expiration_date__lte=thirty_days_from_now,
        expiration_date__gte=today
    ).count()
    expired = reagents.filter(expiration_date__lt=today).count()

    # Adiciona status para cada reagente no contexto
    reagents_with_status = []
    for reagent in reagents:
        status = 'normal'
        if reagent.expiration_date:
            if reagent.expiration_date < today:
                status = 'expired'
            elif reagent.expiration_date <= thirty_days_from_now:
                status = 'warning'
        reagents_with_status.append({
            'reagent': reagent,
            'status': status
        })

    context = {
        'reagents_with_status': reagents_with_status,
        'total_reagents': total_reagents,
        'expiring_soon': expiring_soon,
        'expired': expired,
        'report_date': today,
        'generated_by': request.user.get_full_name() or request.user.username,
    }

    return render(request, 'reagents/report.html', context)
