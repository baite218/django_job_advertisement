from django.urls import path
from .views import UserPostRelationView, PublicationsView, CommentView, CategoryView

urlpatterns = [
    path('post/', PublicationsView.as_view({'get': 'list', 'post': 'create'})),
    path('post/<int:pk>/', PublicationsView.as_view({'put': 'update', 'get': 'retrieve', 'delete': 'destroy'})),

    path('comment/', CommentView.as_view({'get': 'list', 'post': 'create'})),
    path('comment/<int:pk>', CommentView.as_view({'put': 'update', 'delete': 'destroy'})),

    path('relation', UserPostRelationView.as_view({'get': 'list', 'post': 'create'})),
    path('relation/<int:pk>', UserPostRelationView.as_view({'put': 'update', 'delete': 'destroy'})),

    path('category/', CategoryView.as_view({'get': 'list'})),
    path('category/<int:pk>', CategoryView.as_view({'get': 'retrieve'})),

    # path('post', PublicationsView.as_view({'get': 'list'})),
    # path('post/create', PublicationsView.as_view({'post': 'create'})),
    # path('post/<int:pk>', PublicationsView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),

    # path('post/create', PublicationsView.as_view({'post': 'create'})),
    # path('post/', PublicationsView.as_view({'get': 'list'})),
    # path('post/<int:pk>', PublicationsView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
]