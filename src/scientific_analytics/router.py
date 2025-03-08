from rest_framework.routers import DefaultRouter
from apps.scientific_work.views import ScientyficWorkView
from apps.category.views import CategoryViewSet
from apps.status.views import StatusView
from apps.users.views import UserView

router = DefaultRouter()

router.register(r'scientufuc-works', ScientyficWorkView)
router.register(r'category', CategoryViewSet)
router.register(r'scientufuc-works', StatusView)
router.register(r'scientufuc-works', UserView)
