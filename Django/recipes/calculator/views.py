from django.http import HttpResponse
from django.shortcuts import render, reverse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

def home_view(request):
    template_name = 'calculator/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Омлет': reverse(omlet),
        'Паста': reverse(pasta),
        'Бутер': reverse(buter)
    }
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def calcul(request, recip):
    servings = int(request.GET.get('servings', 1))
    dict_rec = {}
    for key in DATA[recip]:
        dict_rec[key] = round(servings * float(DATA[recip][key]), 2)
    return dict_rec


def omlet(request):
    context = {
        "recipe": calcul(request, 'omlet')
    }
    return render(request, 'calculator/index.html', context)


def pasta(request):
    context = {
        "recipe": calcul(request, 'pasta')
    }
    return render(request, 'calculator/index.html', context)


def buter(request):
    context = {
        "recipe": calcul(request, 'buter')
    }
    return render(request, 'calculator/index.html', context)


