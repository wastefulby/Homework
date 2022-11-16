from django.shortcuts import render
from django.http import HttpResponse

from goods.models import GoodsBooks

# Create your views here.

def index(request):
    books = GoodsBooks.objects.all()
    return render(request, template_name='homepage/index.html', context={'books': books})