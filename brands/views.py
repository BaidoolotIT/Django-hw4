from django.shortcuts import render
from brands.models import Brand
from models.models import Model


def brand(request):
    brands = Brand.objects.all()
    models = Model.objects.all()
    data = {
        'brands': brands,
        'models': models
    }
    return render(request, 'bRand.html', context=data)