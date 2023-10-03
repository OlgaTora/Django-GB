from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('client/orders/<int:pk>/<int:limit>/', views.get_orders_by_client, name='orders_by_clients'),
    path('client/products/<int:pk>/<int:period>', views.get_products_by_client, name='client_basket'),
    path('product/<int:pk>', views.get_product, name='product'),
    path('products/', views.get_products_available, name='products_available'),
    path('products/add', views.add_new_product, name='add_new_product'),
    path('order/<int:pk>/', views.get_order, name='order'),
    path('order/status/<str:status>/', views.status_order, name='status_order'),
    path('order/status/update/<int:pk>/<str:status>/', views.update_status, name='update_status'),
    path('client/orders/<int:pk>/', views.get_full_orders_by_client, name='orders_full_by_client'),
]
