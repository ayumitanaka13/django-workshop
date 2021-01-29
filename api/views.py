from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer

# Create your views here.
@api_view(['GET'])
def apiOverviews(request):
    api_urls = {
        'List': 'product/'
    }
    return Response(api_urls)

# for product model
@api_view(['GET'])
def getAllProducts(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

# def Top(request):
#     return HttpResponse("Top")

# def Http(request):
#     return HttpResponse("Hello world")

# def Test(request):
#     return HttpResponse("Test")
