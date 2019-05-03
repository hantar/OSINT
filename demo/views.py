from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from demo.models import Datacrawl
from django.urls import reverse
from django.views import generic
from crawlers.twitterCrawl import *
from crawlers.redditCrawl import *

def index(request):
	num_results = Datacrawl.objects.all().count()
	raw_data = Datacrawl.objects.all().order_by('-added')
	context = {
		'num_results': num_results,
		'raw_data': raw_data
	}
	if request.method == 'POST' and 'twitterCrawl' in request.POST:
		keyword = request.POST['keywordSearch']
		twitterStream(keyword)
		return HttpResponseRedirect(reverse(viewname='index'))
	elif request.method == 'POST' and 'redditCrawl' in request.POST:
		keyword = request.POST['keywordSearch']
		crawlReddit(keyword)
		return HttpResponseRedirect(reverse(viewname='index'))
	else:
		return render(request, 'demo/index.html', context=context)

#def output(request):
#	if request.is_ajax():
#		data = twitterStream()
#		return render(request, 'demo/output.html', {'output': data})
#