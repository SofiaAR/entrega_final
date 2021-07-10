# Create your views here.
from django.http import HttpResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions, generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.utils import timezone

from javali_store_api.models import Product, Store, Brand, Sale, SaleProduct, Category
from javali_store_api.serializers import ProductSerializer, StoreSerializer, BrandSerializer, ContactSerializer


class ProductViewSet(generics.ListAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'name']


class StoreViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    permission_classes = [permissions.IsAuthenticated]


class BrandViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = [permissions.IsAuthenticated]


@api_view(['POST'])
def new_sale(request):
    s = Sale(description='Nueva venta', created=timezone.now())
    s.save()
    products = request.data
    for p in products:
        product = Product.objects.filter(id=p["id"])
        sp = SaleProduct(sale=s, product=product.get())
        sp.save()
    content = {'success'}
    return Response(content, status=status.HTTP_200_OK)


@api_view(['POST'])
def new_contact(request):
    serializer = ContactSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def new_product(request):
    brand = Brand.objects.filter(id=request.data["brand"])
    category = Category.objects.filter(id=request.data["category"])

    p = Product(name=request.data["name"],
                price=request.data["price"],
                quantity=request.data["quantity"],
                category=category.get(),
                brand=brand.get())
    p.save()
    return Response("success", status=status.HTTP_201_CREATED)


@api_view(['GET'])
def get_image(request):
    p = Product.objects.filter(id=1)
    return HttpResponse(p.get().image, content_type="image/png")
