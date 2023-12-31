import logging
import datetime

from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, get_object_or_404
from shop.models import Order, Product, Client
from .forms import AddNewProduct

logger = logging.getLogger(__name__)


def index(request):
    return render(request, 'shop/index_shop.html')


def get_orders_by_client(request, pk, limit):
    """View for get all orders of client by him ID."""
    msg = f'Request for get orders by client {pk}, limit = {limit}'
    logger.info(msg)
    client = get_object_or_404(Client, pk=pk)
    orders = Order.objects.filter(client=client).all()
    orders = orders[:limit]
    info = f'of client {client.name}'
    return render(request,
                  'shop/orders.html',
                  {'client': client, 'orders': orders, 'info': info})


def get_full_orders_by_client(request, pk):
    """View for get all info about orders of client by him ID."""
    msg = f'Request for get all orders info  by client {pk}'
    logger.info(msg)
    client = get_object_or_404(Client, pk=pk)
    orders = Order.objects.filter(client=client).all()
    products = {}
    for order in orders:
        products[order.id] = list(map(Product.to_list, order.product.all()))
    info = f'of client {client.name}'
    return render(request,
                  'shop/orders_with_products.html',
                  {'client': client, 'orders': orders, 'info': info, 'products': products})


def get_order(request, pk):
    """View for get full information about order."""
    order = get_object_or_404(Order, pk=pk)
    products = list(map(Product.to_list, order.product.all()))
    return render(request,
                  'shop/order.html',
                  {'order': order, 'products': products}, )


def get_product(request, pk):
    """View for get full information about product."""
    product = get_object_or_404(Product, pk=pk)
    return render(request,
                  'shop/product.html',
                  {'product': product}, )


def get_products_by_client(request, pk, period):
    """View for get product basket of client by him ID."""
    msg = f'Request for get products by client {pk}'
    logger.info(msg)
    client = get_object_or_404(Client, pk=pk)
    orders = Order.objects.filter(client=client,
                                  order_date__gt=(datetime.date.today() - datetime.timedelta(days=period))).all()
    products = set(product for order in orders for product in order.product.all())
    return render(
        request,
        'shop/client_basket.html',
        {'client': client, 'products': products, 'period': period}
    )


def get_products_available(request):
    """View for get list of available product."""
    quantity = 0
    msg = f'Request for get available products'
    logger.info(msg)
    products = Product.objects.filter(quantity__gt=quantity)
    return render(request,
                  'shop/products.html',
                  {'products': products})


def status_order(request, status):
    """View for ger orders by status."""
    msg = f'Request for get orders by status {status}'
    logger.info(msg)
    orders = Order.objects.filter(status=status)
    info = f'by status = {status}'
    return render(request,
                  'shop/orders.html',
                  {'orders': orders, 'info': info})


def update_status(request, *args, **kwargs):
    """View for update status of order."""
    pk = kwargs.get('pk')
    status = kwargs.get('status')
    msg = f'Request for change order id = {pk}, new status = {status}'
    logger.info(msg)
    order = get_object_or_404(Order, pk=pk)
    order.status = status
    order.save()
    return get_order(request, pk)


def add_new_product(request):
    message = 'Please fill information about new product'
    if request.method == 'POST':
        form = AddNewProduct(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['product_image']
            product_name = form.cleaned_data['product_name']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            quantity = form.cleaned_data['quantity']
            product = Product(
                product_name=product_name,
                description=description,
                price=price,

                quantity=quantity,
                product_image=image)
            fs = FileSystemStorage()
            fs.save(image.name, image)
            product.save()
            message = 'Successfully operation'
    else:
        form = AddNewProduct()
    return render(
        request,
        'shop/add_new_product.html',
        {'form': form, 'message': message}
    )
