from tabnanny import verbose
from django.contrib import admin

from . import models

# Register your models here.

class ReferencesGenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

class ReferencesCurrenсyAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

admin.site.register(models.ReferencesGenre, ReferencesGenreAdmin)
admin.site.register(models.ReferencesCurrenсy, ReferencesCurrenсyAdmin)