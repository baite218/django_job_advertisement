from rest_framework import serializers
from .models import Post, Comments, UserPostRelation, Category
from users.models import Profile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('username', 'phone',)


class PostSerializer(serializers.ModelSerializer):
    # owner = UserSerializer(read_only=True, many=False)

    class Meta:
        model = Post
        fields = '__all__'
    # def create(self, validated_data):
    #     user = self.context.get('request').user
    #     post = Post.objects.create(owner=user, **validated_data)
    #     return post



class UserPostRelationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPostRelation
        fields = ('post', 'like', 'saved',)


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class CommentsSerializer(serializers.ModelSerializer):
    # owner = UserSerializer(read_only=True)
    
    class Meta:
        model = Comments
        fields = '__all__'

    # def create(self, validated_data):
    #     user = self.context.get('request').user
    #     comment = Comments.objects.create(owner=user, **validated_data)
    #     return comment

    # def update(self, instance, validated_data):
    #     data = validated_data.copy()
    #     data.pop('post', None)
    #     for attr, value, in data.items():
    #         setattr(instance, attr, value)
    #     instance.save()
    #     return instance



    # def update(self, instance, validated_data):
    #     for attr, value, in validated_data.items():
    #         setattr(instance, attr, value)
    #     instance.save()
    #     images = self.context.get('request').data.getlist('post_images')
    #     if images:
    #         PublicationImages.objects.filter(publication=instance).delete()
    #         images_list = [PublicationImages(image=item, publication=instance) for item in images]
    #         PublicationImages.objects.bulk_create(images_list)
    #     return instance