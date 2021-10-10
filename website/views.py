from datetime import datetime

from django.shortcuts import render, redirect
from cloudipsp import Api, Checkout

from .models import Product


# Create your views here.
def index(request):
    products = Product.objects.all()
    context = {
        'products': products,
        'collection': 'папа мама я - огромная семья'.split(),
        'string': 'Можно найти всё на www.ya.ru https://www.ya.ru http://ya.ru ya.ru',
        'dct': {'one': 1, 'two': 2, 'three': 3},
        'number': 212,
        'date': datetime.now(),
        'html': '<script>alert(1)</script>'
    }
    return render(request, 'website/index.html', context)


def about(request):
    return render(request, 'website/about.html')


def create(request):
    if request.method == 'POST':
        product = Product(
            name=request.POST.get('name'),
            description=request.POST.get('description'),
            price=request.POST.get('price')
        )
        product.save()
    return render(request, 'website/create.html')


def delete(request, id):
    Product.objects.filter(id=id).delete()
    return redirect('website:index')


def buy(request, id):
    products = Product.objects.get(id=id)

    api = Api(merchant_id=1396424, secret_key='test')
    checkout = Checkout(api=api)
    data = {
        "currency": "RUB",
        "amount": str(products.price) + '00'
    }
    url = checkout.url(data).get('checkout_url')
    return redirect(url)
