from django.views import generic
from django.urls import reverse_lazy
from . import models
from . import forms
from django.contrib.auth.mixins import PermissionRequiredMixin

from references.models import ReferencesAuthor, ReferencesGenre, ReferencesCurrenсy

# Create your views here.

class DetailGoodsBooks(generic.DetailView):
    model = models.GoodsBooks
    template_name = 'goods/detail.html'

class ListGoodsBooks(PermissionRequiredMixin, generic.ListView):
    model = models.GoodsBooks
    permission_required = 'orders.change_order'
    template_name = 'goods/list.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['goods_name'] = 'books'
        context['goods_create'] = 'goods:create-books'
        context['goods_update'] = 'goods:update-books'
        context['goods_detail'] = 'goods:detail-books'
        context['goods_delete'] = 'goods:delete-books'
        return context

class CreateGoodsBooks(PermissionRequiredMixin, generic.CreateView):
    model = models.GoodsBooks
    form_class = forms.GoodsBooksForm
    permission_required = 'orders.change_order'
    template_name = 'goods/edit.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['goods_name'] = 'books'
        # context['refs_author'] = ReferencesAuthor.objects.all()
        # context['refs_genre'] = ReferencesGenre.objects.all()
        # context['refs_currenсy'] = ReferencesCurrenсy.objects.all()
        return context
    success_url = reverse_lazy('goods:list-books')

class UpdateGoodsBooks(PermissionRequiredMixin, generic.UpdateView):
    model = models.GoodsBooks
    form_class = forms.GoodsBooksForm
    permission_required = 'orders.change_order'
    template_name = 'goods/edit.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['goods_name'] = 'books'
        # context['refs_author'] = ReferencesAuthor.objects.all()
        # context['refs_genre'] = ReferencesGenre.objects.all()
        # context['refs_currenсy'] = ReferencesCurrenсy.objects.all()
        return context
    success_url = reverse_lazy('goods:list-books')

class DeleteGoodsBooks(PermissionRequiredMixin, generic.DeleteView):
    model = models.GoodsBooks
    template_name = 'goods/delete.html'
    permission_required = 'orders.change_order'
    success_url = reverse_lazy('goods:list-books')
