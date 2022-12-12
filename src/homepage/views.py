from django.shortcuts import render
from django.views import generic
from django.contrib.auth import authenticate, login

from goods.models import GoodsBooks
from orders.models import Cart
from references.models import ReferencesGenre, ReferencesAuthor
from django.db.models import Q

# Create your views here.


def index(request):
  genre = request.GET.getlist('genre_id')
  author = request.GET.getlist('author_id')
  q_search = request.GET.getlist('q_search')
  books = GoodsBooks.objects.all()

  print(q_search)
  # print(request.user.get_all_permissions())

  if genre and author:
    books = GoodsBooks.objects.filter(genre__in=genre, author__in=author)
  elif genre:
    books = GoodsBooks.objects.filter(genre__in=genre)
  elif author:
    books = GoodsBooks.objects.filter(author__in=author)
  elif q_search:
    books = GoodsBooks.objects.filter(
        Q(name__in=q_search) |
        Q(author__name__in=q_search)
      )
  else:  
    books = GoodsBooks.objects.all()

  cart_id = request.session.get('cart_id')
  genre_search = ReferencesGenre.objects.all()
  author_search = ReferencesAuthor.objects.all()
  
  # if request.user.is_authenticated:
  #   user =request.user
  #   print(user.carts)
  #   cart_id = None
  #   print(cart_id)
  
  if cart_id:
    cart = Cart.objects.get(pk=cart_id)
  else:
    cart = None
  
  return render(
      request,
       template_name='homepage/index.html',
        context={
          'books': books,
          'genre_search': genre_search,
          'author_search': author_search,
          'cart': cart
          })