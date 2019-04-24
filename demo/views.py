from django.shortcuts import render
from django.http import HttpResponse
from demo.models import WebLinks
from django.views import generic


def index(request):
    num_results = WebLinks.objects.all().count()
    webc = WebLinks.objects.all()
    context = {
        'num_results': num_results,
        'webc': webc
    }
    return render(request, 'demo/index.html', context=context)

class WebListView(generic.ListView):
    model = WebLinks
    context_object_name = 'weblinks_list'
    template_name = 'demo/weblinks_list.html'