from django.shortcuts import render
from django.utils.timezone import now
from .models import Lead
from django.db.models import Count
from datetime import date

def today_followups(request):
    leads = Lead.objects.filter(follow_up_date=now().date())
    return render(request, 'followups.html', {'leads': leads})


def dashboard(request):
    total_leads = Lead.objects.count()
    converted_leads = Lead.objects.filter(status='converted').count()
    pending_leads = Lead.objects.exclude(status='converted').count()
    lost_leads = Lead.objects.filter(status='lost').count()
    today_followups = Lead.objects.filter(follow_up_date=date.today())
    context = {
        'total_leads': total_leads,
        'converted_leads': converted_leads,
        'pending_leads': pending_leads,
        'lost_leads': lost_leads,
        'today_followups': today_followups,
    }

    return render(request, 'dashboard.html', context)

def source_analysis(request):
    data = Lead.objects.values('source').annotate(count=Count('id'))

    total_leads = sum(item['count'] for item in data)

    for item in data:
        item['percentage'] = round((item['count'] / total_leads) * 100, 2) if total_leads > 0 else 0

    context = {
        'data': data,
        'total_leads': total_leads
    }

    return render(request, 'source_analysis.html', context)

def all_leads(request):
    leads = Lead.objects.all()

    context = {
        'leads': leads
    }

    return render(request, "all_leads.html", context)
