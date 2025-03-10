from rest_framework.routers import DefaultRouter
from apps.scientific_work.views import ScientyficWorkView
from apps.category.views import CategoryViewSet
from apps.status.views import StatusView
from apps.users.views import UserView
from apps.institution.views import InstitutionListView

router = DefaultRouter()

router.register(r'scientufic-works', ScientyficWorkView)
router.register(r'category', CategoryViewSet)
router.register(r'statuses', StatusView)
router.register(r'users', UserView)
router.register(r'institution', InstitutionListView)
