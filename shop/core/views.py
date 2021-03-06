
from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError
from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework.decorators import action
from .api import fill_favorites
from .models import Favorite, Customer
from .serializers import FavoriteSerializer, CustomerSerializer, FavoriteWithProductsSerializer


class CustomersViewSet(mixins.CreateModelMixin,
                       mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.DestroyModelMixin,
                       viewsets.GenericViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    @action(detail=True, methods=['GET'])
    def favorites(self, request, pk=None):
        try:
            get_object_or_404(Customer, pk=pk)
            favorites = Favorite.objects.filter(customer_id=pk)
            favorites_with_products = fill_favorites(favorites)
            page = self.paginate_queryset(favorites_with_products)
            if page is not None:
                serializer = FavoriteWithProductsSerializer(page, many=True)
                return self.get_paginated_response(serializer.data)
            serializer = FavoriteWithProductsSerializer(favorites_with_products, many=True)
            return Response(status=200, data={'favorites': serializer.data})
        except ValidationError as err:
            return Response(status=400, data={'detail': str(err)})


class FavoritesViewSet(mixins.CreateModelMixin,
                       mixins.DestroyModelMixin,
                       viewsets.GenericViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
