from django.db import models

# Create your models here.

class ReferencesBook(models.Model):
    name = models.CharField(
        verbose_name = 'Genre',
        #max_lenght = 40,
        default = 'null'
        # blank = True,
        # Null = True
    )
    description = models.TetxField(
        blank = True,
        Null = True
    )

# class ReferencesBook2(models.Model):
#     name = models.CharField(
#         verbose_name = 'ТЕСТ'
#         max_lenght = 40,
#         default = 'null'
#         # blank = True,
#         # Null = True
#     )
#     description = models.TetxField(
#         blank = True,
#         Null = True
#     )