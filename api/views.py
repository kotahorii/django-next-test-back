from rest_framework import viewsets, generics
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from . import serializers
from .models import Blog


class CreateUserView(generics.CreateAPIView):
    serializer_class = serializers.UserSerializer
    permission_classes = (AllowAny,)


class BlogReadOnlyView(viewsets.ReadOnlyModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = serializers.TagSerializer
    permission_classes = (AllowAny,)


class DeleteBlogView(generics.DestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = serializers.BlogSerializer()
