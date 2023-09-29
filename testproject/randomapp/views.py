import logging
import random
from django.http import HttpResponse
from django.shortcuts import render
from randomapp.models import HeadsOrTails

logger = logging.getLogger(__name__)


def index(request):
    return render(request, 'index_random.html')


def get_cube(request, rolls):
    res_list = {}
    for roll in range(1, rolls + 1):
        side = random.randint(1, 6)
        res_list[f'roll {roll} result = '] = side
    context = {'results': res_list, 'game': 'cube'}
    msg = f'Side of cube is {res_list}'
    logger.info(msg)
    return render(request, 'game_result.html', context)
    # return HttpResponse(msg)


def get_number(request, rolls):
    res_list = {}
    for roll in range(1, rolls + 1):
        num = random.randint(0, 100)
        res_list[f'roll {roll} result = '] = num
    context = {'results': res_list, 'game': 'numbers'}
    res = f'Number is {res_list}'
    logger.info(res)
    return render(request, 'game_result.html', context)
    # return HttpResponse(msg)


def get_tails(request):
    attempt = HeadsOrTails(result=random.choice(['heads', 'tails']))
    attempt.save()
    logger.info(attempt)
    n = request.GET.get('n', '5')
    res = HeadsOrTails.result_stat(n)
    return HttpResponse(res.items())


def get_heads(request, rolls):
    res_list = {}
    for roll in range(1, rolls + 1):
        attempt = HeadsOrTails(result=random.choice(['heads', 'tails']))
        res_list[f'roll {roll} result = '] = attempt
    context = {'results': res_list, 'game': 'head or tails'}
    res = f'Number is {res_list}'
    logger.info(res)
    return render(request, 'game_result.html', context)
