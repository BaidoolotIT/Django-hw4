from django.shortcuts import render
from models.models import Model
from brands.models import Brand


def model(request, brand_id):
    brands = Brand.objects.get(id=brand_id)
    models = Model.objects.filter(model_id=brands)

    data = {
        'models': models,
        'brands': brands
    }
    return render(request, 'mOdel.html', context=data)



