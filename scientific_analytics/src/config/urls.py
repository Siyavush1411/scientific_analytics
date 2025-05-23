from django.contrib import admin
from django.urls import path, include
from .router import router
from rest_framework_simplejwt.views import TokenRefreshView
from apps.users.views import RegisterView, UserTokenObtainPairView, ProfileView
from apps.institution.views import InstitutionDetailView, InstitutionListCreateView
from core.services.views import ScientificWorkStatsAPI, UserStatsAPI, InstitutionStatsAPI
from apps.scientific_work.views import upload_files

from django.conf import settings
from django.conf.urls.static import static
from apps.users.utils.synchronize_users import synch
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import re_path
from rest_framework import permissions


schema_view = get_schema_view(
    openapi.Info(
        title='API Docs',
        default_version='V1',
        description='dick for api',
        ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    )

urlpatterns = [
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", UserTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path('institutions/', InstitutionListCreateView.as_view(), name='institution-list'),
    path('institutions/<int:pk>/', InstitutionDetailView.as_view(), name='institution-detail'),
    path('api/stats/institutions/', InstitutionStatsAPI.as_view()),
    path('api/stats/works/', ScientificWorkStatsAPI.as_view()),
    path('api/stats/users/', UserStatsAPI.as_view()),
    path('sync-authors/', synch, name='sync-authors'),
    path('upload/', upload_files),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
