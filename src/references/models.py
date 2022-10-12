from django.db import models

# Create your models here.

class ReferencesGenre(models.Model):
    name = models.CharField(
        verbose_name = 'Genre',
        max_length = 40,
        default = 'null'
        # blank = True,
        # Null = True
    )
    description = models.TextField(
        blank = True,
        null = True
    )

class ReferencesCurrenсy(models.Model):
    name = models.CharField(
        verbose_name = 'Currenсy',
        max_length = 40,
        default = 'null'
        # blank = True,
        # Null = True
    )
    description = models.TextField(
        blank = True,
        null = True
    )