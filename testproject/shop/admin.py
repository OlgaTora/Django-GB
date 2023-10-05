import csv
import decimal
from django.contrib import admin
from django.http import HttpResponse

from .models import Product, Order, Client


class OrderInline(admin.TabularInline):
    model = Order


class ClientAdmin(admin.ModelAdmin):
    inlines = [
        OrderInline,
    ]
    list_display = ['name', 'mail', 'phone', 'registration_date']
    ordering = ['-registration_date']
    list_filter = ['name', 'registration_date']
    readonly_fields = ['name', 'registration_date']
    search_fields = ['name']
    search_help_text = 'Search client by name'
    fieldsets = [
        (
            'Main client information',
            {
                'classes': ['wide'],
                'description': 'main information',
                'fields': ['name', 'registration_date'],
            },
        ),
        (
            'Contact information',
            {
                'classes': ['wide'],
                'description': 'contacts',
                'fields': [('phone', 'mail'), 'address'],
            },
        ),
    ]


@admin.action(description='Price +10')
def price_plus_10(modeladmin, request, queryset):
    for product in queryset:
        product.price = product.price * decimal.Decimal('1.1')
        product.save()


class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'price', 'quantity']
    ordering = ['product_name']
    list_filter = ['product_name']
    readonly_fields = ['product_name', 'added_date']
    search_fields = ['description']
    search_help_text = 'Search product by description'
    list_per_page = 10
    actions = [price_plus_10]
    fieldsets = [
        (
            'Main product information',
            {
                'classes': ['wide'],
                'description': 'main information',
                'fields': ['product_name', 'description', 'added_date'],
            },
        ),
        (
            'Financial product information',
            {
                'classes': ['wide'],
                'description': 'financial information',
                'fields': ['price', 'quantity'],
            },
        ),
    ]


@admin.action(description='Download orders in csv format')
def download_orders_2csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="orders.csv"'
    writer = csv.writer(response)
    writer.writerow(['Date', 'Summa', 'Status'])
    orders = queryset.values_list('order_date', 'order_summ', 'status')
    for order in orders:
        writer.writerow(order)
    return response


@admin.action(description='Update status for PAID')
def update_status_paid(modeladmin, request, queryset):
    queryset.update(status='paid')


class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_date', 'order_summ', 'status']
    ordering = ['-order_date']
    list_filter = ['order_date', 'status']
    readonly_fields = ['order_date', 'client']
    search_fields = ['product']
    search_help_text = 'Search order by product'
    list_per_page = 10
    actions = [update_status_paid, download_orders_2csv]
    fieldsets = [
        (
            'Main order information',
            {
                'classes': ['wide'],
                'description': 'main information',
                'fields': ['order_date', 'order_summ', 'status'],
            },
        ),
        (
            'Personal order information',
            {
                'classes': ['wide'],
                'description': 'details of order',
                'fields': ['client', 'product'],
            },
        ),
    ]


admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Client, ClientAdmin)
