import logging
import random
from django.http import HttpResponse
from django.shortcuts import render
from randomapp.models import HeadsOrTails
from .forms import ChoiceGameForm

logger = logging.getLogger(__name__)


def index(request):
    return render(request, 'randomapp/index_random.html')


def choice_form(request):
    if request.method == 'POST':
        form = ChoiceGameForm(request.POST)
        if form.is_valid():
            game = form.cleaned_data['game']
            print(game)
            rolls = form.cleaned_data['rolls']
            match game:
                case 'cube':
                    return get_cube(request, rolls)
                case 'num':
                    return get_number(request, rolls)
                case 'h_or_t':
                    return get_heads(request, rolls)
            logger.info(f'Input {game=}, {rolls=}')
    else:
        form = ChoiceGameForm()
        return render(request,
                      'randomapp/choice_form.html',
                      {'form': form})


def get_cube(request, rolls):
    res_list = {}
    for roll in range(1, rolls + 1):
        side = random.randint(1, 6)
        res_list[f'roll {roll} result = '] = side
    context = {'results': res_list, 'game': 'cube'}
    msg = f'Side of cube is {res_list}'
    logger.info(msg)
    return render(request, 'randomapp/game_result.html', context)
    # return HttpResponse(msg)


def get_number(request, rolls):
    res_list = {}
    for roll in range(1, rolls + 1):
        num = random.randint(0, 100)
        res_list[f'roll {roll} result = '] = num
    context = {'results': res_list, 'game': 'numbers'}
    res = f'Number is {res_list}'
    logger.info(res)
    return render(request, 'randomapp/game_result.html', context)
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
    res = f'Result is {res_list}'
    logger.info(res)
    return render(request, 'randomapp/game_result.html', context)
