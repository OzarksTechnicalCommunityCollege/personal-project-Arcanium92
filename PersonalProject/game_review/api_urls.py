from rest_framework.routers import DefaultRouter
from .views import GameReviewSets

router = DefaultRouter()
router.register(r'reviews', GameReviewSets)

urlpatterns = router.urls