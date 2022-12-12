from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin

from . import models, forms
from goods import  models as goods_models

# Create your views here.

# class PassRequestToFormViewMixin:
#     def get_form_kwargs(self):
#         kwargs = super().get_form_kwargs()
#         kwargs['request'] = self.request
#         return kwargs

def view_cart(request):
    context = {} 

    if request.method == 'POST':
        book_pk = int(request.POST.get('book_pk'))
        quantity = int(request.POST.get('quantity'))
        user = request.user
        
        print(book_pk)
        print(quantity)
        print(user.carts)
        
        if book_pk and quantity:
            cart_id = request.session.get('cart_id')
                        
            if request.user.is_authenticated:
                user = request.user
            else:
                user = None

            cart, created = models.Cart.objects.get_or_create(
                pk=cart_id,
                defaults={
                    'user': user
                }
            )
            print(user)
            print (cart.pk)
            if created:
                request.session['cart_id'] = cart.pk
                
            cart_id = cart.pk
            print (cart_id)
            book = goods_models.GoodsBooks.objects.get(pk=book_pk)
            price = book.price

            book_in_cart, created = models.BookinCart.objects.get_or_create(
                book=book,
                cart=cart,
                defaults={
                    'quantity': quantity,
                    'price': price
                }
            )
            
            if not created:
                change_quantity = request.POST.get('change_quantity')
                if change_quantity != None:
                    book_in_cart.quantity = int(change_quantity)
                else:
                    book_in_cart.quantity += quantity
                book_in_cart.save()                     
    else:
        cart_id = request.session.get('cart_id') 

    cart = models.Cart.objects.get(pk=cart_id)
    # print(cart)
    context['cart'] = cart
    context['form'] = forms.OrderForm(
        request=request,
        view_order = True
        )
    return render(
        request, 
        template_name='orders/view_cart.html',
        context = context            
        )

class CreateOrder(generic.CreateView):
    model = models.Order
    template_name ='orders/order_complete.html'
    form_class = forms.OrderForm
    success_url = reverse_lazy('orders:order-complete')

    def form_valid(self, form):
        cart_id = self.request.session.get('cart_id')
        cart = models.Cart.objects.get(pk=cart_id)
        form.instance.cart = cart
        return super().form_valid(form)

    def get_success_url(self) -> str:
        del self.request.session['cart_id']
        return super().get_success_url()
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        cart_id = self.request.session.get('cart_id')
        if cart_id:
            cart = models.Cart.objects.get(pk=cart_id)
            context['cart'] = cart

        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        view_order = False
        kwargs.update({'request': self.request, 'view_order': view_order})
        return kwargs

class UserOrders(generic.ListView):
    model = models.Order
    template_name = 'orders/user_orders.html'
    success_url = reverse_lazy('orders:user-orders')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        user = self.request.user
        print(user)
        cart = user.carts.all()
        print(cart)
        context['cart'] = cart

        return context

def edit_cart(request):
    context = {} 

    if request.method == 'POST':
        book_pk = int(request.POST.get('book_pk'))
        change_quantity = int(request.POST.get('change_quantity'))
        order_pk = int(request.POST.get('order_pk'))
        print(book_pk)
        print(order_pk)
        print(change_quantity)
        if book_pk and change_quantity:
            book_in_cart = models.BookinCart.objects.get(pk=book_pk)
            book_in_cart.quantity = int(change_quantity)
            book_in_cart.save()

    orders = models.Order.objects.all()
    context['orders'] = orders
    return render(
        request,
        # template_name='orders/orders_update/order_pk',
        template_name='orders/orders_list.html',
        context = context
    ) 

class UpdateOrder(PermissionRequiredMixin, generic.UpdateView):
    model = models.Order
    template_name ='orders/order_update.html'
    form_class = forms.OrderForm
    permission_required = 'orders.change_order'
    success_url = reverse_lazy('orders:orders-list')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        
        cart_id = self.object.cart.pk
        print(cart_id + 20000)
        cart = models.Cart.objects.get(pk=cart_id)
        order_pk = self.object.pk
        print(order_pk)
        context['cart'] = cart
        context['order_pk'] = order_pk
        # orders = models.Order.objects.all()
        # context['orders'] = orders
        print(cart.order.status)
        print(cart.order.phone)
        
        # object_temp = context.get('object')
        # print(object_temp)
        # object_temp.status = cart.order.status
        # object_temp.phone = cart.order.phone
        # object_temp.name = cart.order.name
        # object_temp.adress = cart.order.adress
        # object_temp.email = cart.order.email
        # object_temp.info = cart.order.info
        # del context['form']
        # context['form'] = forms.OrderForm(instance=object_temp, request=self.request)
        # context['form'] = form
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        view_order = False
        kwargs.update({'request': self.request, 'view_order': view_order})
        return kwargs

class ListOrders(PermissionRequiredMixin, generic.ListView):
    model =models.Order
    template_name ='orders/orders_list.html'
    permission_required = 'orders.change_order'
    success_url = reverse_lazy('orders:orders-list')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        orders = models.Order.objects.all()
        context['orders'] = orders
        return context

class DeleteCartBook(generic.DeleteView):
    model = models.BookinCart
    template_name ='orders/view_cart.html'
    success_url = reverse_lazy('orders:view-cart') 