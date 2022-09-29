from django.db import models
# Create your models here.


class Brand(models.Model):
    name = models.CharField(max_length=50, null=True)
    image = models.ImageField(upload_to='brand_image', null=True, blank=True)

    def __str__(self):
        return self.name
