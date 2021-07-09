from django.contrib import admin
from .models import Post, Comments, UserPostRelation, Category

admin.site.register(Post)
admin.site.register(UserPostRelation)
admin.site.register(Comments)
admin.site.register(Category)