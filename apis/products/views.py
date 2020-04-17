from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView

from django.shortcuts import render
from django.shortcuts import redirect

from apis.products.serializers import CategorySerializer, Sub_CategorySerializer, ProductSerializer
from apis.products.models import Category, Sub_Category, Product


@api_view(['GET'])
@renderer_classes([JSONRenderer, TemplateHTMLRenderer,])
def home(request):
    products = Product.objects.all()
    print(products)
    if request.accepted_renderer.format == 'html':
        print('show html')
        data = {'products': products}
        return Response(data, template_name='base.html')

    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
@renderer_classes([TemplateHTMLRenderer,JSONRenderer,] )
def create_products(request):
    if request.accepted_renderer.format=='html':
        if request.method=='GET':
            print('inside get')
            serializer = ProductSerializer()
            print('---------------')
            return Response({'serializer': serializer}, template_name='create_products.html')
        elif request.method=='POST':
            print(dir(request))
            print(request.query_params)
            serializer = ProductSerializer(data=request.data)
            print(serializer.initial_data)
            print(serializer.is_valid())
            print(serializer.errors)
            if serializer.is_valid():
                print('valid serializer product')
                serializer.save()
                return redirect('home')





@api_view(['GET', 'POST'])
@renderer_classes([TemplateHTMLRenderer,JSONRenderer,] )
def detail_product(request, id, slug):
    if request.accepted_renderer.format=='html':
        if request.method=='GET':
            print('inside get')
            product = Product.objects.get(id=id)
            # serializer = ProductSerializer(product)
            print('---------------')
            data = {'product': product}
            return Response(data, template_name='detail_product.html')





@api_view(['GET', 'POST'])
@renderer_classes([TemplateHTMLRenderer,JSONRenderer,] )
def update_product(request, id, slug):
    product = Product.objects.get(id=id)
    if request.accepted_renderer.format=='html':
        if request.method=='GET':
            print('inside get')
            serializer = ProductSerializer(product)
            print('---------------')
            return Response({'serializer': serializer}, template_name='update_product.html')
        elif request.method=='POST':
            print(dir(request))
            print(request.query_params)
            serializer = ProductSerializer(product, data=request.data)
            print(serializer.initial_data)
            print(serializer.is_valid())
            print(serializer.errors)
            if serializer.is_valid():
                print('valid serializer product')
                serializer.save()
                return redirect('home')




@api_view(['GET', 'POST'])
@renderer_classes([TemplateHTMLRenderer,])
def create_category(request):
    if request.accepted_renderer.format=='html':
        if request.method=='GET':
            print('inside get')
            serializer = CategorySerializer()
            print('---------------')
            return Response({'serializer': serializer}, template_name='create_products.html')
        elif request.method=='POST':
            serializer = CategorySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return redirect('home')

@api_view(['GET', 'POST'])
@renderer_classes([TemplateHTMLRenderer,])
def create_sub_category(request):
    if request.accepted_renderer.format=='html':
        if request.method=='GET':
            print('inside get')
            serializer = Sub_CategorySerializer()
            print('---------------')
            return Response({'serializer': serializer}, template_name='create_products.html')
        elif request.method=='POST':
            serializer = Sub_CategorySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return redirect('home')








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




