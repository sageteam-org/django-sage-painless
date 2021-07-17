"""
Auto Generated views.py
You may need to change some parts
"""

from django.http import Http404

from rest_framework.viewsets import ModelViewSet


from products.models.category import Category

from products.models.product import Product

from products.models.discount import Discount

from products.api.serializers import (
    CategorySerializer,
    ProductSerializer,
    DiscountSerializer,

)


class CategoryViewset(ModelViewSet):
    """
    Category Viewset
    Auto generated
    """
    serializer_class = CategorySerializer
    
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
    
    model_class = Category

    def get_queryset(self):
        """
        get queryset from cache
        """
        return self.model_class.get_all_from_cache()

    def get_object(self):
        """
        get object from cache
        """
        queryset = self.get_queryset()
        if len(queryset) == 0:
            raise Http404('Not Found')
        obj = queryset[0]
        return obj
    

class ProductViewset(ModelViewSet):
    """
    Product Viewset
    Auto generated
    """
    serializer_class = ProductSerializer
    
    model_class = Product

    def get_queryset(self):
        """
        get queryset from cache
        """
        return self.model_class.get_all_from_cache()

    def get_object(self):
        """
        get object from cache
        """
        queryset = self.get_queryset()
        if len(queryset) == 0:
            raise Http404('Not Found')
        obj = queryset[0]
        return obj
    

class DiscountViewset(ModelViewSet):
    """
    Discount Viewset
    Auto generated
    """
    serializer_class = DiscountSerializer
    
    model_class = Discount

    def get_queryset(self):
        """
        get queryset from cache
        """
        return self.model_class.get_all_from_cache()

    def get_object(self):
        """
        get object from cache
        """
        queryset = self.get_queryset()
        if len(queryset) == 0:
            raise Http404('Not Found')
        obj = queryset[0]
        return obj
    
