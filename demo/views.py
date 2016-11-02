from django.shortcuts import render
from django.http import HttpResponse
import logging
logger = logging.getLogger('mylogger')
def test(request):
    context  = {}
    context['hello'] = 'Hello World!'
    logger.info("-------dghsdghsd------------")
    return render(request, 'test.html', context)

    # return HttpResponse("this is successful ,congratulation!")



