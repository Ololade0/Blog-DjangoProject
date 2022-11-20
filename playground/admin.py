from django.contrib import admin
from . import models


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'unit_price']
    list_editable = ['unit_price']
    list_per_page = 10
    list_select_related = ['collection']


def collection_title(product):
    return product.collection.title


@admin.display(ordering='inventory')
def inventory_status(product):
    if product.inventory < 10:
        return 'Low'
    return 'OK'


@admin.register(models.Order)
class OderAdmin(admin.ModelAdmin):
    list_display = ['id', 'placed_at', 'payment_status', 'customer']


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'membership']
    list_editable = ['membership']
    ordering = ['first_name', 'last_name']
    list_per_page = 10


# @admin.register(models.Order)
# class OrderAdmin(admin.ModelAdmin):
#     list_display = ['placed_at', 'id']


admin.site.register(models.Collection)

# Register your models here.
