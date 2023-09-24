import logging
import random
from django.http import HttpResponse
from randomapp.models import HeadsOrTails

logger = logging.getLogger(__name__)


def get_cube(request):
    side = random.randint(1, 6)
    res = f'Side of cube is {side}'
    logger.info(res)
    return HttpResponse(res)


def get_number(request):
    num = random.randint(0, 100)
    res = f'Number is {num}'
    logger.info(res)
    return HttpResponse(res)


def get_tails(request):
    attempt = HeadsOrTails(result=random.choice(['heads', 'tails']))
    attempt.save()
    logger.info(attempt)
    n = request.GET.get('n', '5')
    res = HeadsOrTails.result_stat(n)
    return HttpResponse(res.items())
