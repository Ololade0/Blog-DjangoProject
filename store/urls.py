from django.urls import path
from . import views
from pprint import pprint
from rest_framework_nested import routers

# app_name = "store"
router = routers.DefaultRouter()
router.register('products', views.ProductViewSet,basename='products')
pprint(router.urls)
product_router = routers.NestedDefaultRouter(router,'products', lookup= 'product_pk')
product_router.register('reviews', views.ReviewSet, basename='product-reviews')

urlpatterns = router.urls + product_router.urls



