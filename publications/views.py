from django.shortcuts import render
from rest_framework.views import APIView, Response

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, status

from .permissions import IsPostOwnerOrReadOnly, IsCommentsOwnerOrReadOnly
from .models import Post, Comments, UserPostRelation, Category
from .serializers import UserPostRelationSerializer, CommentsSerializer, PostSerializer, CategorySerializer


       

class UserPostRelationView(ModelViewSet):
    queryset = UserPostRelation.objects.all()
    serializer_class = UserPostRelationSerializer
    permission_classes = (IsAuthenticated, )
    lookup_field = 'pk'
    filter_backends = [filters.SearchFilter]
    search_fields = ['post']

class CommentView(ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    permission_classes = (IsCommentsOwnerOrReadOnly, )
    lookup_field = 'pk'
    filter_backends = [filters.SearchFilter]
    search_fields = ['post']


class CategoryView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'pk'
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']




class PublicationsView(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # permission_classes = (IsPostOwnerOrReadOnly, ) 
    lookup_field = 'pk'

    # def get_object(self):
    #     obj = Post.objects.prefetch_related().annotate(
    #         owner_nick_name=F('owner__username'),
    #     ).get(id=self.kwargs['pk'])
    #     self.check_object_permissions(self.request, obj)
    #     return obj


    # def list(self, request, *args, **kwargs):
    #     user = request.user
    #     # Post = self.get_object()
    #     if Post.owner == user:
    #         return super().retrieve(request, *args, **kwargs)
    #     return Response('нет доступа', status=status.HTTP_403_FORBIDDEN)

    # def create(self, request, *args, **kwargs):
    #     user = request.user
    #     if Post.objects.filter(owner=user, id=Post):
    #         return super().create(request, *args, **kwargs)
    #     return Response('нет доступа', status=status.HTTP_403_FORBIDDEN)

    # # def update(self, request, *args, **kwargs):
    #     user = request.user
    #     Post = self.get_object()
    #     if Post.owner == user:
    #         return super().update(request, *args, **kwargs)
    #     return Response('нет доступа', status=status.HTTP_403_FORBIDDEN)

    # def destroy(self, request, *args, **kwargs):
    #     user = request.user
    #     Post = self.get_object()
    #     if Post.owner == user:
    #         self.perform_destroy(Post)
    #         return Response(status=status.HTTP_204_NO_CONTENT)
    #     return Response('нет доступа', status=status.HTTP_403_FORBIDDEN)