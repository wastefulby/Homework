from dataclasses import fields
from django import forms
from . import models


class GoodsBooksForm(forms.ModelForm):
    class Meta:
        model = models.GoodsBooks
        fields = '__all__'
