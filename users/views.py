from django.contrib.auth import authenticate

from rest_auth.models import TokenModel
from rest_framework import status
from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django.shortcuts import render

from .serializers import (
	# UserRegisterSerializer,  UserLoginSerializer, 
	ProfileSerializer, ProfessionSerializer, 
	ProfileResumeSerializer, SubscriberSerializer)
from .permissions import IsUserOwnerOrReadOnly
from .models import Profile, Professions, ProfileResume, Subscriber




class ProfileView(ModelViewSet):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    # permission_classes = (IsUserOwnerOrReadOnly, )
    lookup_field = 'pk'

# class UserRegisterView(CreateAPIView):
#     serializer_class = UserRegisterSerializer

# class UserLoginView(GenericAPIView):
#     serializer_class = UserLoginSerializer

#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         username = serializer.data.get('username')
#         first_name = serializer.data.get('first_name')
#         password = serializer.data.get('password')
#         user = authenticate(request, first_name=first_name, password=password)
#         if user:
#             token = TokenModel.objects.get(user=user)
#             return Response({'key': token.key}, status=status.HTTP_201_CREATED)
#         return Response('invalid login', status=status.HTTP_401_UNAUTHORIZED)


class ProfessionView(ModelViewSet):
    queryset = Professions.objects.all()
    serializer_class = ProfessionSerializer
    permission_classes = (IsUserOwnerOrReadOnly, ) 
    lookup_field = 'pk'


class SubscriberView(ModelViewSet):
    queryset = Subscriber.objects.all()
    lookup_field = 'pk'
    serializer_class = SubscriberSerializer


class ResumeView(ModelViewSet):
    queryset = ProfileResume.objects.all()
    serializer_class = ProfileResumeSerializer
    permission_classes = (IsUserOwnerOrReadOnly, ) 
    lookup_field = 'pk'

def auth(request):
    return render(request, 'oauth.html')