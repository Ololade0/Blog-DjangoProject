from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from playground.models import Product, OrderItem, Order, Customer, Collection
from playground.models import Product


def say_hello(request):
    try:
        Product.objects.count()
        # retrieving object method
        # all method get all the object in a given table
        Product.objects.all()
        # to get a single method with id in a given table, get method will be use, it doesnt retun a query set
        product = Product.objects.get(pk=1)
    except ObjectDoesNotExist:
        pass
    return render(request, 'hello.html', {'name': 'Ololade'})


# def filtering_data(request):
#     Product.objects.filter(inventory__lt=0, unit_price__lt=20)
#     queryset = Product.objects.filter(unit_price=20)
#     return render(request, 'hello.html', {'name': 'Ololade'})


# TO SAVE/CREATE OBJECT
def create_object(request):
    collection = Collection()
    collection.title = 'Video Games'
    collection.featured_product = Product(pk=1)
    collection.save()


# ANOTHER METHOD FOR SAVING/CREATING OBJECT
# Collection.objects.create(title="a", featured_product_id=1)

# TO UPDATE OBJECT
def update_object(request):
    Collection.objects.filter(pk=11).update(featured_product=None)


# ANOTHER METHOD FOR UPDATING OBJECT
# collection = Collection(pk=11)
# collection.title = 'Games'
# collection.featured_product = None
# collection.save()

def delete_object(request):
    collection = Collection(pk=11)
    collection.delete()

    # TO DELETE OBJECT WHOSE ID IS GREATER THAN 5
    Collection.objects.filter(id__gt=5).delete()
