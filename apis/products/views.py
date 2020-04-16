from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from rest_framework.response import Response
from rest_framework.generics import ListAPIView

from django.shortcuts import render

from apis.products.serializers import CategorySerializer
from apis.products.models import Category


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




@api_view(['GET'])
@renderer_classes([JSONRenderer,TemplateHTMLRenderer,])

def list_category(request):

    """
    A view that can return JSON or HTML representations
    of the users in the system.
    """
    categories = Category.objects.all()

    if request.accepted_renderer.format == 'html':
        # print('no template')
        # TemplateHTMLRenderer takes a context dict,
        # and additionally requires a 'template_name'.
        # It does not require serialization.
        data = {'categories': categories}
        print('in template')
        print(data)
        return Response(data, template_name='base.html')
    print('out template')
    # JSONRenderer requires serialized data as normal.
    serializer = CategorySerializer(categories, many=True)
    data = serializer.data
    return Response(data)



