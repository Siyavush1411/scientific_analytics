from django.contrib import admin
from django.urls import path, include
from .router import router
from rest_framework_simplejwt.views import TokenRefreshView
from apps.users.views import RegisterView, UserTokenObtainPairView, ProfileView
from apps.institution.views import InstitutionDetailView, InstitutionListCreateView
from core.services.views import ScientificWorkStatsAPI, UserStatsAPI, InstitutionStatsAPI
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
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
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
