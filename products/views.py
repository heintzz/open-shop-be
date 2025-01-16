from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from products.serializers import ProductSerializer
from django.http import Http404

from .models import Product


class ProductList(APIView):
    def post(self, request):
        product = ProductSerializer(
            data=request.data, context={'request': request})
        if product.is_valid():
            product.save()
            return Response(product.data, status=status.HTTP_201_CREATED)

        return Response(product.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        name = request.query_params.get("name")
        location = request.query_params.get("location")

        product = Product.objects.all()

        if name:
            product = product.filter(name__icontains=name)
        if location:
            product = product.filter(location=location)

        serializer = ProductSerializer(
            product, many=True, context={'request': request})
        return Response({"products": serializer.data}, status=status.HTTP_200_OK)


class ProductDetail(APIView):
    def get(self, request, id):
        product = self.get_object(id)
        if product is None:
            return Response(
                {"error": "Product not found"},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, id):
        product = self.get_object(id)
        if product is None:
            return Response(
                {"error": "Product not found"},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = ProductSerializer(
            product, data=request.data,  context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        product = self.get_object(id)
        if product is None:
            return Response(
                {"error": "Product not found"},
                status=status.HTTP_404_NOT_FOUND
            )
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_object(self, id):
        try:
            return Product.objects.get(pk=id)
        except Product.DoesNotExist:
            return None
