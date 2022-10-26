from django.db import models
from django.urls import reverse_lazy

# Create your models here.

class ReferencesAuthor(models.Model):
    name = models.CharField(
        verbose_name = 'Author',
        max_length = 40,
        default = 'null'
    )
    description = models.TextField(
        blank = True,
        null = True
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        #return f'/list/author'
        return reverse_lazy('references:list-author')

    # def success_url(self):
    #     return f'/list/'

class ReferencesGenre(models.Model):
    name = models.CharField(
        verbose_name = 'Genre',
        max_length = 40,
        default = 'null'
    )
    description = models.TextField(
        blank = True,
        null = True
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        #return f'/list/genre'
        return reverse_lazy('references:list-genre')

    # def success_url(self):
    #     return f'/list/'

class ReferencesCurrenсy(models.Model):
    name = models.CharField(
        verbose_name = 'Currenсy',
        max_length = 20,
        default = 'null'
    )
    description = models.TextField(
        blank = True,
        null = True
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        #return f'/list/currenсy'
        return reverse_lazy('references:list-currenсy')

    # def success_url(self):
    #     return f'/list/'