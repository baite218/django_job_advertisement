from django.contrib.auth import get_user_model
from rest_auth.models import TokenModel
from rest_framework import serializers

from .models import Profile, Professions, ProfileResume, Subscriber




class ProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Profile
        fields = ('__all__')
        
# class UserLoginSerializer(serializers.Serializer):
#     first_name = serializers.CharField()
#     password = serializers.CharField()


# class UserRegisterSerializer(serializers.Serializer):
#     username = serializers.CharField()
#     password = serializers.CharField(write_only=True)
#     first_name = serializers.CharField()
#     last_name = serializers.CharField()
#     email = serializers.EmailField(required=False)
#     phone = serializers.CharField(required=False)

#     def create(self, validated_data):
#         password = validated_data.pop('password')
#         user = Profile.objects.create(**validated_data)
#         user.set_password(password)
#         user.save()
#         TokenModel.objects.create(user=user)
#         return user



class ProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professions
        fields = ('__all__')
   

class ProfileResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileResume
        fields = ('__all__')


class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = ('__all__')

