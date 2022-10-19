from django.db import models

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
        return f'/author/list_a/'

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
        return f'/genre/list_g/'

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
        return f'/currenсy/list_c/'

    # def success_url(self):
    #     return f'/list/'