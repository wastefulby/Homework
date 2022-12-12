from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin
from . import models
from . import forms

# Create your views here.

#Author
class DetailReferencesAuthor(generic.DetailView):
    model = models.ReferencesAuthor
    template_name = 'references/detail.html'

class ListReferencesAuthor(PermissionRequiredMixin, generic.ListView):
    model = models.ReferencesAuthor
    permission_required = 'orders.change_order'
    template_name = 'references/list.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['ref_name'] = 'author'
        context['ref_create'] = 'references:create-author'
        context['ref_update'] = 'references:update-author'
        context['ref_detail'] = 'references:detail-author'
        context['ref_delete'] = 'references:delete-author'
        return context

class CreateReferencesAuthor(PermissionRequiredMixin, generic.CreateView):
    model = models.ReferencesAuthor
    form_class = forms.ReferencesAuthorForm
    permission_required = 'orders.change_order'
    template_name = 'references/edit.html'

class UpdateReferencesAuthor(PermissionRequiredMixin, generic.UpdateView):
    model = models.ReferencesAuthor
    form_class = forms.ReferencesAuthorForm
    permission_required = 'orders.change_order'
    template_name = 'references/edit.html'

class DeleteReferencesAuthor(PermissionRequiredMixin, generic.DeleteView):
    model = models.ReferencesAuthor
    permission_required = 'orders.change_order'
    template_name = 'references/delete.html'
    success_url = reverse_lazy('references:list-author')

#Genre
class DetailReferencesGenre(PermissionRequiredMixin, generic.DetailView):
    model = models.ReferencesGenre
    permission_required = 'orders.change_order'
    template_name = 'references/detail.html'

class ListReferencesGenre(PermissionRequiredMixin, generic.ListView):
    model = models.ReferencesGenre
    permission_required = 'orders.change_order'
    template_name = 'references/list.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['ref_name'] = 'genre'
        context['ref_create'] = 'references:create-genre'
        context['ref_update'] = 'references:update-genre'
        context['ref_detail'] = 'references:detail-genre'
        context['ref_delete'] = 'references:delete-genre'
        return context

class CreateReferencesGenre(PermissionRequiredMixin, generic.CreateView):
    model = models.ReferencesGenre
    form_class = forms.ReferencesGenreForm
    permission_required = 'orders.change_order'
    template_name = 'references/edit.html'

class UpdateReferencesGenre(PermissionRequiredMixin, generic.UpdateView):
    model = models.ReferencesGenre
    form_class = forms.ReferencesGenreForm
    permission_required = 'orders.change_order'
    template_name = 'references/edit.html'

class DeleteReferencesGenre(PermissionRequiredMixin, generic.DeleteView):
    model = models.ReferencesGenre
    permission_required = 'orders.change_order'
    template_name = 'references/delete.html'
    success_url = reverse_lazy('references:list-genre')

#Currenсy
class DetailReferencesCurrenсy(PermissionRequiredMixin, generic.DetailView):
    model = models.ReferencesCurrenсy
    permission_required = 'orders.change_order'
    template_name = 'references/detail.html'

class ListReferencesCurrenсy(PermissionRequiredMixin, generic.ListView):
    model = models.ReferencesCurrenсy
    permission_required = 'orders.change_order'
    template_name = 'references/list.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['ref_name'] = 'currenсy'
        context['ref_create'] = 'references:create-currenсy'
        context['ref_update'] = 'references:update-currenсy'
        context['ref_detail'] = 'references:detail-currenсy'
        context['ref_delete'] = 'references:delete-currenсy'
        return context

class CreateReferencesCurrenсy(PermissionRequiredMixin, generic.CreateView):
    model = models.ReferencesCurrenсy
    form_class = forms.ReferencesCurrenсyForm
    permission_required = 'orders.change_order'
    template_name = 'references/edit.html'

class UpdateReferencesCurrenсy(PermissionRequiredMixin, generic.UpdateView):
    model = models.ReferencesCurrenсy
    form_class = forms.ReferencesCurrenсyForm
    permission_required = 'orders.change_order'
    template_name = 'references/edit.html'

class DeleteReferencesCurrenсy(PermissionRequiredMixin, generic.DeleteView):
    model = models.ReferencesCurrenсy
    permission_required = 'orders.change_order'
    template_name = 'references/delete.html'
    success_url = reverse_lazy('references:list-currenсy')
