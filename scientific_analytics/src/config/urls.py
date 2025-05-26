from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

from .router import router
from apps.users.views import (
    RegisterView,
    UserTokenObtainPairView,
    ProfileView,
    upload_avatar,
    get_current_user,
)
from apps.institution.views import InstitutionDetailView, InstitutionListCreateView
from core.services.views import (
    ScientificWorkStatsAPI,
    UserStatsAPI,
    InstitutionStatsAPI,
)
from apps.scientific_work.views import upload_files
from apps.users.utils.synchronize_users import synch
from rest_framework_simplejwt.views import TokenRefreshView

schema_view = get_schema_view(
    openapi.Info(
        title='API Docs',
        default_version='v1',
        description='API Documentation',
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    re_path(r'^api/docs/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('admin/', admin.site.urls),

    path('api/', include(router.urls)),

    path('api/register/', RegisterView.as_view(), name="register"),
    path('api/login/', UserTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path('api/token/refresh/', TokenRefreshView.as_view(), name="token_refresh"),
    path('api/profile/', ProfileView.as_view(), name="profile"),
    path('api/get_current_user/', get_current_user),
    path('api/upload_avatar/', upload_avatar),

    path('api/institutions/', InstitutionListCreateView.as_view(), name='institution-list'),
    path('api/institutions/<int:pk>/', InstitutionDetailView.as_view(), name='institution-detail'),

    path('api/stats/institutions/', InstitutionStatsAPI.as_view()),
    path('api/stats/works/', ScientificWorkStatsAPI.as_view()),
    path('api/stats/users/', UserStatsAPI.as_view()),

    path('api/upload/', upload_files),
    path('api/sync-authors/', synch, name='sync-authors'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
