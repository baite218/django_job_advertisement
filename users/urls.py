from django.urls import path
from users.views import ProfessionView, ProfileView, ResumeView, SubscriberView

urlpatterns = [
    path('profiles', ProfileView.as_view({'get': 'list'})),
    path('profiles/<int:pk>/', ProfileView.as_view({'put': 'update', 'get': 'retrieve', 'delete': 'destroy'})),

    path('profession/', ProfessionView.as_view({'get': 'list', 'post': 'create'})),
    path('profession/<int:pk>/', ProfessionView.as_view({'put': 'update', 'get': 'retrieve', 'delete': 'destroy'})),

    path('rusume', ResumeView.as_view({'get': 'list'})),
    path('rusume/<int:pk>', ResumeView.as_view({'put': 'update', 'delete': 'destroy'})),

    path('subscribles', SubscriberView.as_view({'get': 'list'})),
    path('subscribles/<int:pk>', SubscriberView.as_view({'put': 'update', 'delete': 'destroy'})),
]