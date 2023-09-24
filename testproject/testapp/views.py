import logging
from django.http import HttpResponse

logger = logging.getLogger(__name__)


def index(request):
    log_msg = 'Index page accessed'
    logger.info(log_msg)
    return HttpResponse("Hello, world!")
