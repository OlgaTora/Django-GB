from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('orders_by_clients/<int:pk>/<int:limit>/', views.get_orders_by_client, name='orders_by_clients'),
    path('products/', views.get_products_available, name='products_available'),
    path('status_order/<str:status>/', views.status_order, name='status_order'),
    path('update_status/<int:pk>/<str:status>/', views.update_status, name='update_status'),
]