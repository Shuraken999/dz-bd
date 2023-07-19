from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort_pages = request.GET.get('sort', '')
    sort_phones = Phone.objects.all()
    if sort_pages == 'max_price':
        phones = sort_phones.order_by('-price')
        context = {'phones': phones}
        return render(request, template, context)
    elif sort_pages == 'min_price':
        phones = sort_phones.order_by('price')
        context = {'phones': phones}
        return render(request, template, context)
    elif sort_pages == 'name':
        phones = sort_phones.order_by('name')
        context = {'phones': phones}
        return render(request, template, context)
    context = {'phones': sort_phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phones = Phone.objects.filter(slug=slug)
    for phone in phones:
        context = {'phones': phone}
    return render(request, template, context)


