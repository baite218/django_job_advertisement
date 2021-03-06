from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsPostOwnerOrReadOnly(BasePermission):
   def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            return True
        return obj == request.user


class IsCommentsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        elif request.method == 'DELETE':
            return obj.owner == request.user or obj.books.owner == request.user
        return obj.owner == request.user