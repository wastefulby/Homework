from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import generic
from . import models
from . import forms

# Create your views here.

#Genre
class DetailReferencesGenre(generic.DetailView):
    model = models.ReferencesGenre
    template_name = 'references/detail_g.html'

class ListReferencesGenre(generic.ListView):
    model = models.ReferencesGenre
    template_name = 'references/list_g.html'

class CreateReferencesGenre(generic.CreateView):
    model = models.ReferencesGenre
    form_class = forms.ReferencesGenreForm
    template_name = 'references/create_g.html'

class UpdateReferencesGenre(generic.UpdateView):
    model = models.ReferencesGenre
    form_class = forms.ReferencesGenreForm
    template_name = 'references/update_g.html'

class DeleteReferencesGenre(generic.DeleteView):
    model = models.ReferencesGenre
    template_name = 'references/delete_g.html'
    success_url = '/genre/list_g/'

#Author
class DetailReferencesAuthor(generic.DetailView):
    model = models.ReferencesAuthor
    template_name = 'references/detail_a.html'

class ListReferencesAuthor(generic.ListView):
    model = models.ReferencesAuthor
    template_name = 'references/list_a.html'

class CreateReferencesAuthor(generic.CreateView):
    model = models.ReferencesAuthor
    form_class = forms.ReferencesAuthorForm
    template_name = 'references/create_a.html'

class UpdateReferencesAuthor(generic.UpdateView):
    model = models.ReferencesAuthor
    form_class = forms.ReferencesAuthorForm
    template_name = 'references/update_a.html'

class DeleteReferencesAuthor(generic.DeleteView):
    model = models.ReferencesAuthor
    template_name = 'references/delete_a.html'
    success_url = '/author/list_a/'

#Currenсy
class DetailReferencesCurrenсy(generic.DetailView):
    model = models.ReferencesCurrenсy
    template_name = 'references/detail_c.html'

class ListReferencesCurrenсy(generic.ListView):
    model = models.ReferencesCurrenсy
    template_name = 'references/list_c.html'

class CreateReferencesCurrenсy(generic.CreateView):
    model = models.ReferencesCurrenсy
    form_class = forms.ReferencesCurrenсyForm
    template_name = 'references/create_c.html'

class UpdateReferencesCurrenсy(generic.UpdateView):
    model = models.ReferencesCurrenсy
    form_class = forms.ReferencesCurrenсyForm
    template_name = 'references/update_c.html'

class DeleteReferencesCurrenсy(generic.DeleteView):
    model = models.ReferencesCurrenсy
    template_name = 'references/delete_c.html'
    success_url = '/currenсy/list_c/'
