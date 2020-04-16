from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView

from django.shortcuts import render

from apis.products.serializers import CategorySerializer, Sub_CategorySerializer, ProductSerializer
from apis.products.models import Category, Sub_Category, Product


class ListCategoryAPIView(ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    # def get_queryset(self):
    #     return Category.objects.all()

@api_view(['GET'])
@renderer_classes([JSONRenderer,])
def list_ct(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def check(request):
    if request.method == 'GET':
        return Response({'Hey': 'Hey'})
    elif request.method == 'POST':
        return Response({'postt': 'postt'})

@api_view(['GET', 'POST'])
def create_user(request):
    if request.method == 'GET':
        pass
    elif request.metho == 'POST':
        pass




@api_view(['GET', 'POST'])
@renderer_classes([JSONRenderer,TemplateHTMLRenderer,])

def list_category(request):

    categories = Category.objects.all()
    sub_categories = Sub_Category.objects.all()
    products = Product.objects.all()


    if request.accepted_renderer.format == 'html':
        data = {'categories': categories, 'sub_categories': sub_categories, 'products': products}
        print('in template')
        print(data)
        return Response(data, template_name='base.html')
    print('out template')
    # JSONRenderer requires serialized data as normal.
    serializer1 = CategorySerializer(categories, many=True)
    serializer2 = Sub_CategorySerializer(sub_categories, many=True)
    serializer3 = ProductSerializer(products, many=True)
    data = [serializer1.data, serializer2.data, serializer3.data]
    return Response(data)


# @api_view(['GET','POST'])
# def create_user(request):


# class CreateUserAPIView(CreateAPIView):
#     serailizer_class = User




