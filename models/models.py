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


