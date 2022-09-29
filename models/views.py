from django.shortcuts import render
from models.models import Model, Series
from brands.models import Brand


def model(request, brand_id):
    brands = Brand.objects.get(id=brand_id)
    models = Model.objects.filter(model_id=brands)

    data = {
        'models': models,
        'brands': brands,
    }
    return render(request, 'mOdel.html', context=data)


def series(request, model_id, brand_id):
    brands = Brand.objects.get(id=brand_id)
    models = Model.objects.get(id=model_id)
    series1 = Series.objects.filter(model=model_id)

    data = {
        'series': series1,
        'models': models,
        'brands': brands
    }

    return render(request, 'series.html', context=data)

