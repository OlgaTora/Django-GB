import logging
from django.shortcuts import render

logger = logging.getLogger(__name__)


def index(request):
    logger.info('Index page accessed')
    context = {'name': 'Stan Smith'}
    return render(request, "me/index.html", context)
#    return render(request, 'me/index.html')


def about(request):
    logger.info('Index page accessed')
    context = {'some_text': 'Tssssssssssssssssss'}
    return render(request, "me/about.html", context)
#    return render(request, 'me1/about.html')
