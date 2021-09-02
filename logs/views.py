from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.http import JsonResponse
from django.shortcuts import render

from logs.models import Log, Category


@login_required(login_url='accounts:login')
def visualize(request):
    logs = Log.objects.only(
        'timestamp',
        'message',
        'category__name',
    ).select_related("category").order_by('-timestamp')[:10]

    return render(request, 'logs/index.html', {'logs': logs})


@login_required(login_url='accounts:login')
def log_count(request):
    _log_count = Log.objects.all().values('timestamp').annotate(count=Count('pk', distinct=True))

    _data = [{'name': lc.get('timestamp').strftime("%b %d %H:%M:%S"), 'y': lc.get('count')} for lc in _log_count]

    return JsonResponse({'log_count': _data})


@login_required(login_url='accounts:login')
def category_count(request):
    # sort: largest -> smallest
    categories = Category.objects.all().annotate(logs_count=Count('logs')).order_by('-logs_count')

    # format data for highcharts
    _data = [{'name': i.name, 'y': i.logs_count} for i in categories]

    return JsonResponse({'categories': _data})
