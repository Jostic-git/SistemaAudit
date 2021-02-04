from django.urls import path, include
from rest_framework.routers import SimpleRouter

from ethiccertification.views import EthicItemViewSet

router = SimpleRouter()
router.register('item', EthicItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
