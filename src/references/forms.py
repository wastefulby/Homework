from dataclasses import fields
from django import forms
from . import models


class ReferencesAuthorForm(forms.ModelForm):
    class Meta:
        model = models.ReferencesAuthor
        fields = '__all__'

class ReferencesGenreForm(forms.ModelForm):
    class Meta:
        model = models.ReferencesGenre
        fields = '__all__'

class ReferencesCurrenсyForm(forms.ModelForm):
    class Meta:
        model = models.ReferencesCurrenсy
        fields = '__all__'