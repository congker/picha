from  django.http import HttpResponse
from django.shortcuts import render
import logging
from django.template import RequestContext
from django.template.loader import render_to_string
from django.shortcuts import render_to_response
logger=logging.getLogger('defalut')


def index(request):
    template_name = 'index.html'
    context  = {}
    hello = 'Nginx welcome you!'
    HttpResponse("test just")
    return render_to_response(template_name, RequestContext(request,
                                                          {"hello": hello}))
    # return render(request, 'test.html', context)