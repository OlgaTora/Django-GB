from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=200)
    mail = models.EmailField()
    phone = models.CharField(max_length=50)
    address = models.TextField()
    registration_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    product_name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(default=0, decimal_places=2, max_digits=10)
    quantity = models.IntegerField(default=0)
    added_date = models.DateField(auto_now_add=True)
    product_image = models.ImageField(default=None, blank=True, null=True)

    def __str__(self):
        return f'Product: {self.product_name} quantity: {self.quantity}'

    def to_list(self):
        return f'{self.product_name}'


class Order(models.Model):
    class Status(models.TextChoices):
        DELIVERED = 'delivered'
        PAID = 'paid'
        ON_ROAD = 'on road'
        CANCEL = 'cancelled'
        CREATE = 'created'

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)
    order_summ = models.DecimalField(decimal_places=2, max_digits=10)
    order_date = models.DateField(auto_now_add=True)
    status = models.CharField(choices=Status.choices, max_length=50, default=Status.CREATE)

    def __str__(self):
        return (f'Date: {self.order_date}'
                f' Summa: {self.order_summ},'
                f' Products: {list(map(Product.to_list, self.product.all()))}'
                f' Client: {self.client},'
                f' Status: {self.status}\n')
