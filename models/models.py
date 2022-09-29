from django.db import models
from brands.models import Brand
# Create your models here.

#создал модельки
class Model(models.Model):
    name = models.CharField(max_length=50, null=True)
    engine = models.CharField(max_length=40, null=True)
    hp = models.IntegerField(null=True)
    nm = models.IntegerField(null=True)
    model = models.ForeignKey(Brand, null=True, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='model_image', null=True, blank=True)

    def __str__(self):
        return self.name


class Series(models.Model):
    # objects = None
    s_name = models.CharField(max_length=50)
    engine_s = models.CharField(max_length=40)
    hp_s = models.IntegerField()
    nm_s = models.IntegerField()
    model = models.ForeignKey(Model, null=True, on_delete=models.CASCADE)
    image_s = models.ImageField(upload_to='series_image', null=True, blank=True)

    def __str__(self):
        return self.s_name