from django.shortcuts import render
from django.http import HttpResponse
from demo.models import WebCrawler


def index(request):
    num_results = WebCrawler.objects.all().count()
    context = {
        'num_results': num_results
    }
    return render(request, 'demo/index.html', context=context)
