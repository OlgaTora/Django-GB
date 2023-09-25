import logging
from django.http import HttpResponse
from hwapp2.models import Order, Product, Client
logger = logging.getLogger(__name__)


def index(request):
    return HttpResponse("Welcome to hw2")


def get_orders_by_client(request, pk, limit):
    """View for get all orders of client by him ID."""
    msg = f'Request for get orders by client {pk}, limit = {limit}'
    logger.info(msg)
    client_id = Client.objects.filter(pk=pk).first()
    orders = Order.objects.filter(client_id=client_id).all()
    return HttpResponse(orders[:limit])


def get_products_available(request):
    """View for get list of available product."""
    quantity = 0
    msg = f'Request for get available products'
    logger.info(msg)
    products = Product.objects.filter(quantity__gt=quantity)
    return HttpResponse(products)


def status_order(request, status):
    """View for ger orders by status."""
    msg = f'Request for get orders by status {status}'
    logger.info(msg)
    orders = Order.objects.filter(status=status)
    return HttpResponse(orders)


def update_status(request, *args, **kwargs):
    """View for update status of order."""
    pk = kwargs.get('pk')
    status = kwargs.get('status')
    msg = f'Request for change order id = {pk}, new status = {status}'
    logger.info(msg)
    order = Order.objects.filter(pk=pk).first()
    order.status = status
    order.save()
    return HttpResponse(order)
