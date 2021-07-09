from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_auth.views import LoginView
from rest_auth.registration.views import RegisterView
# from users.views import UserRegisterView, UserLoginView, auth

urlpatterns = [
	path('admin/', admin.site.urls),

    # path('profile/register', UserRegisterView.as_view()),
    # path('profile/login', UserLoginView.as_view()),

    path('signin/', LoginView.as_view(), name = 'rest_login'),
    path('signup/', RegisterView.as_view(), name = 'rest_register'),
    
    path('users/', include('users.urls')),
    path('posts/', include('publications.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
