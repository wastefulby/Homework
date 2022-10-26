from django.views import generic
from django.urls import reverse_lazy
from . import models
from . import forms

# Create your views here.

#Author
class DetailReferencesAuthor(generic.DetailView):
    model = models.ReferencesAuthor
    template_name = 'references/detail.html'

class ListReferencesAuthor(generic.ListView):
    model = models.ReferencesAuthor
    template_name = 'references/list-author.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['ref_name'] = 'author'
        return context

class CreateReferencesAuthor(generic.CreateView):
    model = models.ReferencesAuthor
    form_class = forms.ReferencesAuthorForm
    template_name = 'references/edit.html'

class UpdateReferencesAuthor(generic.UpdateView):
    model = models.ReferencesAuthor
    form_class = forms.ReferencesAuthorForm
    template_name = 'references/edit.html'

class DeleteReferencesAuthor(generic.DeleteView):
    model = models.ReferencesAuthor
    template_name = 'references/delete.html'
    success_url = reverse_lazy('references:list-author')

#Genre
class DetailReferencesGenre(generic.DetailView):
    model = models.ReferencesGenre
    template_name = 'references/detail.html'

class ListReferencesGenre(generic.ListView):
    model = models.ReferencesGenre
    template_name = 'references/list-genre.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['ref_name'] = 'author'
        return context

class CreateReferencesGenre(generic.CreateView):
    model = models.ReferencesGenre
    form_class = forms.ReferencesGenreForm
    template_name = 'references/edit.html'

class UpdateReferencesGenre(generic.UpdateView):
    model = models.ReferencesGenre
    form_class = forms.ReferencesGenreForm
    template_name = 'references/edit.html'

class DeleteReferencesGenre(generic.DeleteView):
    model = models.ReferencesGenre
    template_name = 'references/delete.html'
    success_url = reverse_lazy('references:list-genre')

#Currenсy
class DetailReferencesCurrenсy(generic.DetailView):
    model = models.ReferencesCurrenсy
    template_name = 'references/detail.html'

class ListReferencesCurrenсy(generic.ListView):
    model = models.ReferencesCurrenсy
    template_name = 'references/list-currenсy.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['ref_name'] = 'currenсy'
        return context

class CreateReferencesCurrenсy(generic.CreateView):
    model = models.ReferencesCurrenсy
    form_class = forms.ReferencesCurrenсyForm
    template_name = 'references/edit.html'

class UpdateReferencesCurrenсy(generic.UpdateView):
    model = models.ReferencesCurrenсy
    form_class = forms.ReferencesCurrenсyForm
    template_name = 'references/edit.html'

class DeleteReferencesCurrenсy(generic.DeleteView):
    model = models.ReferencesCurrenсy
    template_name = 'references/delete.html'
    success_url = reverse_lazy('references:list-currenсy')
