from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer


from apis.accounts.models import User
from apis.accounts.serializers import UserCreateSerializer, UserUpdateSerializer


@api_view(['GET', 'POST'])
@renderer_classes([TemplateHTMLRenderer,])
def create_user(request):
    if request.accepted_renderer.format == 'html':
        if request.method == 'GET':
            serializer = UserCreateSerializer()
            return Response({'serializer': serializer},template_name='user.html')
        elif request.method == 'POST':
            serializer = UserCreateSerializer(data = request.data)
            if serializer.is_valid():
                serializer.create(serializer.data)
                print('valid serializer')
            return Response({'success': 'success'},template_name='base.html')


@api_view(['GET', 'POST'])
@renderer_classes([TemplateHTMLRenderer,])
def update_user(request, id):
    user = User.objects.get(id=id)
    if request.accepted_renderer.format == 'html':
        if request.method == 'GET':
            serializer = UserUpdateSerializer()
            serializer.instance = user
            return Response({'serializer': serializer},template_name='user.html')
        elif request.method == 'POST':
            # password = request.data.pop('password')
            serializer = UserUpdateSerializer(user, data = request.data, partial=True)
            if serializer.is_valid():
                print('valid serialzer')
                serializer.update(serializer.data)
            return Response({'success': 'success'},template_name='base.html')

