from django.views import generic
from django.urls import reverse_lazy
from . import models
from . import forms

from references.models import ReferencesAuthor, ReferencesGenre, ReferencesCurrenсy

# Create your views here.

class DetailGoodsBooks(generic.DetailView):
    model = models.GoodsBooks
    template_name = 'goods/detail.html'

class ListGoodsBooks(generic.ListView):
    model = models.GoodsBooks
    template_name = 'goods/list.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['goods_name'] = 'books'
        context['goods_create'] = 'goods:create-books'
        context['goods_update'] = 'goods:update-books'
        context['goods_detail'] = 'goods:detail-books'
        context['goods_delete'] = 'goods:delete-books'
        return context

class CreateGoodsBooks(generic.CreateView):
    model = models.GoodsBooks
    form_class = forms.GoodsBooksForm
    template_name = 'goods/edit.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['goods_name'] = 'books'
        # context['refs_author'] = ReferencesAuthor.objects.all()
        # context['refs_genre'] = ReferencesGenre.objects.all()
        # context['refs_currenсy'] = ReferencesCurrenсy.objects.all()
        return context
    success_url = reverse_lazy('goods:list-books')

class UpdateGoodsBooks(generic.UpdateView):
    model = models.GoodsBooks
    form_class = forms.GoodsBooksForm
    template_name = 'goods/edit.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['goods_name'] = 'books'
        # context['refs_author'] = ReferencesAuthor.objects.all()
        # context['refs_genre'] = ReferencesGenre.objects.all()
        # context['refs_currenсy'] = ReferencesCurrenсy.objects.all()
        return context
    success_url = reverse_lazy('goods:list-books')

class DeleteGoodsBooks(generic.DeleteView):
    model = models.GoodsBooks
    template_name = 'goods/delete.html'
    success_url = reverse_lazy('goods:list-books')
