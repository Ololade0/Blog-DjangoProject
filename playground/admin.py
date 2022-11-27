from django.contrib import admin, messages
from django.db.models import Count
from django.utils.html import format_html, urlencode
from django.urls import reverse
from . import models


@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'products_count']
    # OVERRIDING OF BASE QUERY WHEN ITS NOT INCLUDED ON THE OBJECT FIELD
    @admin.display(ordering='products')
    def products_count(self, collection):
        # return collection.products_count
        # TO REVERSE
        url = reverse('admin:store_product_changelist') + '?'
        var = + urlencode({
            'collection__id': str(collection.id)
        })
        # PROVIDING LINKS TO OTHER PAGES, THE RETURN WILL BE HTML FORMAT
        return format_html('<a href="https://google.com">{} </a>', url, collection.products_count)

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            products_count=Count('product')
        )


    # TO CREATE CUSTOM FILTER
class InventoryFilter(admin.SimpleListFilter):
    title = 'inventory'
    parameter_name = 'inventory'

    def lookups(self, request, model_admin):
        return [
            ('<10', 'Low')
        ]

    def queryset(self, request, queryset):
        if self.value() == '<10':
            return queryset.filter(inventory__lt=10)



@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    # fields = ['title', 'slug']
    prepopulated_fields = {
        'slug': ['title']
    }
    actions = ['clear_inventory']
    list_display = ['title', 'unit_price', 'inventory_status', 'collection']
    list_editable = ['unit_price']
    list_filter = ['collection', 'last_update', InventoryFilter]
    list_per_page = 10
    list_select_related = ['collection']

    @admin.display(ordering='inventory')
    def inventory_status(self, product):
        if product.inventory < 45:
            return 'Low'
        return 'OK'


    def collection_title(self, product):
      return product.collection.title


    def clear_inventory(self, request, queryset):
        updated_count = queryset.update(inventory=0)
        self.message_user(
            request, f'{updated_count} products were successfully updated',
            messages.ERROR
        )





@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'membership']
    list_editable = ['membership']
    ordering = ['first_name', 'last_name']
    list_per_page = 10
    search_fields = ['first_name__istartswith', 'last_name__istartswith']


@admin.display(ordering='inventory')
def inventory_status(product):
    if product.inventory < 10:
        return 'Low'
    return 'OK'


@admin.register(models.Order)
class OderAdmin(admin.ModelAdmin):
    list_display = ['id', 'placed_at', 'payment_status', 'customer']
