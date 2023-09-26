import logging
from django.shortcuts import render

logger = logging.getLogger(__name__)


def index(request):
    logger.info('Index page accessed')
    context = {'name': 'Stan Smith'}
    return render(request, "hwapp1/index.html", context)
#    return render(request, 'hwapp1/index.html')


def about(request):
    logger.info('Index page accessed')
    context = {'some_text': 'Tssssssssssssssssss'}
    return render(request, "hwapp1/about.html", context)
#    return render(request, 'hwapp1/about.html')
