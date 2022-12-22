from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from playground.models import Product, Collection, OrderItem
from .models import Review
from .serializers import ProductSerializers, CollectionSerializers, ReviewSerializer


# TO GET ALL Product
class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializers

    def get_queryset(self):
        queryset = Product.objects.all()
        collection_id = self.request.query_params.get('collection_id')
        if collection_id is not None:
            queryset = queryset.filter(collection_id=collection_id)
            return queryset


    def get_serializer_context(self):
        return {'request': self.request}

    def destroy(self, request, *args, **kwargs):
        if OrderItem.objects.filter(product_id=kwargs['pk']).count() > 0:
            return Response({'error': 'Product cannot be deleted'})
        return super().destroy(request, *args, **kwargs)


#
# class CollectionViewSet(ModelViewSet):
#     queryset = Collection.objects.annotate(
#         products_count = Count('products')).all()
#     serializer_class = CollectionSerializers
#
#     def  delete(self, request, pk):
#         collection = get_object_or_404(Collection, pk=pk)
#         if collection.product_set.count() > 0:
#             return Response({'error': 'Collection cannot be deleted'})
#         collection.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#

class ReviewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
