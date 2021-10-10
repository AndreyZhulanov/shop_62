from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField('Название продукта', max_length=30)
    description = models.TextField('Описание продукта')
    price = models.IntegerField('Цена продукта')

    def __str__(self):
        return self.name
