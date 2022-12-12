from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
statuses = (
    ('In progress', "In progress"),
    ('Sended', "Sended"),
    ('Done', "Done"),
)

# Create your models here.


class Cart(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name='User cart',
        related_name='carts',
        on_delete=models.PROTECT,
        null=True,
        blank=True
    )
    def total_quantity(self):
        all_books_in_cart = self.book.all()
        total_quantity = 0
        for books_quantity in all_books_in_cart:
            total_quantity += books_quantity.quantity
        return total_quantity

    def total_price(self):
        total_price_in_cart = self.book.all()
        total_price = 0
        for price in total_price_in_cart:
            total_price += price.price_per_position()
        return total_price

    # def __str__(self):
    #     return self.user

class BookinCart(models.Model):
    book = models.ForeignKey(
        "goods.GoodsBooks",
        verbose_name='Book in a cart',
        on_delete=models.PROTECT,
    )
    cart = models.ForeignKey(
        "orders.Cart",
        verbose_name='Cart',
        related_name='book',
        on_delete=models.PROTECT,
    )
    quantity = models.IntegerField(
        verbose_name='Quantity',
        default=1
    )
    price = models.DecimalField(
        max_digits=5,
        decimal_places=2,
    )
    create_date = models.DateTimeField(
        "Create date",
        auto_now=False,
        auto_now_add=True
    )
    update_date = models.DateTimeField(
        "Update date",
        auto_now=True,
        auto_now_add=False
    )
    def price_per_position(self):
        return self.price * self. quantity

    def __str__(self):
        return self.book

class Order(models.Model):
    status = models.CharField(
        verbose_name='Status',
        max_length=20,
        choices=statuses,
        default='In progress'
    )
    cart = models.OneToOneField(
        "orders.Cart",
        verbose_name='Cart',
        related_name='order',
        on_delete=models.PROTECT,
    )
    phone = models.CharField(
        verbose_name='Phone',
        max_length=50,
    )
    name = models.CharField(
        verbose_name='Name',
        max_length=20
    )
    adress = models.CharField(
        verbose_name='Adress',
        max_length=100,
    )
    email = models.EmailField(
        verbose_name='Email',
        max_length=100,
    )
    info = models.TextField(
        verbose_name='Info',
        max_length=500,
    )
    create_date = models.DateTimeField(
        "Create date",
        auto_now=False,
        auto_now_add=True
    )
    update_date = models.DateTimeField(
        "Update date",
        auto_now=True,
        auto_now_add=False
    )
