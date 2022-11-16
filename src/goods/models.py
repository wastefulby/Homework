from django.db import models
from django.urls import reverse_lazy

from references.models import ReferencesAuthor, ReferencesGenre, ReferencesCurrenсy

#from . import models

# Create your models here.

class GoodsBooks(models.Model):
    name = models.CharField(
        verbose_name = 'Name',
        max_length = 40,
        default = 'null'
    )
    author = models.ForeignKey(
        ReferencesAuthor,
        on_delete = models.PROTECT,
        max_length = 40,
        default = 'null'
    )
    genre = models.ForeignKey(
        ReferencesGenre,
        on_delete = models.PROTECT,
        max_length = 40,
        default = 'null'
    )
    currenсy = models.ForeignKey(
        ReferencesCurrenсy,
        on_delete = models.PROTECT,
        max_length = 20,
        default = 'null'
    )
    cover = models.ImageField(
        verbose_name = 'Book cover',
        blank = True,
        null = True,        
        upload_to = 'uploads'
    )
    price = models.DecimalField(
        max_digits = 5,
        decimal_places = 2,
        default = 0.00
    )
    rating = models.FloatField(
        default = 0
    )
    description = models.TextField(
        blank = True,
        null = True
    )

    def __str__(self):
        return self.name