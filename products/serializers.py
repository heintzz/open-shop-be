from rest_framework import serializers
from products.models import Product
from rest_framework.reverse import reverse


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    _links = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'name', 'sku', 'description', 'shop',
                  'location', 'price', 'discount', 'category',
                  'stock', 'is_available', 'picture', '_links']

    def get__links(self, obj):
        request = self.context.get('request')
        return [
            {
                "rel": "self",
                "href": reverse('product-list'),
                "action": "POST",
                "types": ["application/json"]
            },
        ]
