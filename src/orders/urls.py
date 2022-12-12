from django.urls import path, re_path
from . import views


app_name = "orders"

urlpatterns = [
    path('cart/', views.view_cart, name='view-cart'),
    path('edit_cart/', views.edit_cart, name='edit-cart'),
    path('delete/<int:pk>/', views.DeleteCartBook.as_view(), name='delete-cart'),
    path('order_complete/', views.CreateOrder.as_view(), name='order-complete'),
    path('user_orders/', views.UserOrders.as_view(), name='user-orders'),
    path('order_update/<int:pk>/', views.UpdateOrder.as_view(), name='order-update'),
    path('orderslist/', views.ListOrders.as_view(), name='orders-list'),
   
]
