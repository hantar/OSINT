from django.shortcuts import render
from django.http import HttpResponse
from demo.models import WebLinks
from django.views import generic


def index(request):
    num_results = WebLinks.objects.all().count()
    raw_data = WebLinks.objects.all()
    webc = WebLinks.objects.all()
    context = {
        'num_results': num_results,
        'webc': webc,
        'raw_data': raw_data
    }

    return render(request, 'demo/index.html', context=context)

