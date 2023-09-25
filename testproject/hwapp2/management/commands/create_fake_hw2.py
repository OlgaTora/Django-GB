import random
from django.core.management.base import BaseCommand
from hwapp2.models import Client, Product, Order


class Command(BaseCommand):
    help = "Generate fake data base."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Fake DB')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            client = Client(
                name=f'Name_{i}',
                mail=f'mail{i}@yandex.ru',
                phone=random.randint(1000000000, 9999999999),
                address=f'Address of Name_{i}',
            )
            client.save()
            product = Product(
                product_name=f'product_{i}',
                description=f'description of product_{i}',
                price=random.uniform(0.01, 10000000),
                quantity=random.randint(0, 100)
            )
            product.save()

        for j in range(1, count**2 + 1):
            order = Order(
                client=random.choice(Client.objects.all()),
                order_summ=random.uniform(0.01, 10000000),
                status=random.choice(Order.Status.choices)[0]
            )
            order.save()

            random_products = random.randint(1, count)
            for _ in range(random_products):
                query = random.choice(Product.objects.all())
                order.product.add(query)
                order.save()
