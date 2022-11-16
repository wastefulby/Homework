from django.contrib import admin
from . import models

# Register your models here.

class GoodsBooksAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'genre', 'currenсy', 'cover', 'price', 'rating', 'description')

admin.site.register(models.GoodsBooks, GoodsBooksAdmin)