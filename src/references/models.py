from django.db import models

# Create your models here.

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