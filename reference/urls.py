from django.urls import path, include
from rest_framework.routers import SimpleRouter

from reference.views import CompanyViewSet, RiskViewSet, ProcessViewSet, SubProcessViewSet

router = SimpleRouter()
router.register('company', CompanyViewSet)
router.register('risk', RiskViewSet)
router.register('process', ProcessViewSet)
router.register('subprocess', SubProcessViewSet)

urlpatterns = [
    path('', include(router.urls)),
    #path('user/', return_domen_user),
]
