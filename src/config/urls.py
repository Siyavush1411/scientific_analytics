from django.contrib import admin
from django.urls import path, include
from .router import router
from apps.users.views import RegisterView, TokenObtainPairView, ProfileView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
    path("token/refresh", TokenObtainPairView.as_view(), name="token_refresh"),
    path("profile/", ProfileView.as_view(), name="profile")
]
