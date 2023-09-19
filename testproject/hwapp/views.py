import logging
from django.shortcuts import render

logger = logging.getLogger(__name__)


def index(request):
    logger.info('Index page accessed')
    return render(request, 'hwapp/index.html')


def about(request):
    logger.info('Index page accessed')
    return render(request, 'hwapp/about.html')
