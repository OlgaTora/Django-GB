import logging
import random
from django.http import HttpResponse
from django.shortcuts import render

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
    num = random.choice(['heads', 'tails'])
    res = f'{num} wins'
    logger.info(res)
    return HttpResponse(res)
