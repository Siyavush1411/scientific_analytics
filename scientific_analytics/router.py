from rest_framework.routers import DefaultRouter
from apps.scientific_work.views import ScientyficWorkView

router = DefaultRouter()

router.register(r'scientufuc-works', ScientyficWorkView)
