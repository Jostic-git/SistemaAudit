from django.urls import path, include
from rest_framework.routers import SimpleRouter

from hotline.views import HotLineItemViewSet, CategoryHotLineViewSet, SubCategoryHotLineViewSet, HotLineCommentViewSet, \
    HotLineFileViewSet

router = SimpleRouter()
router.register('item', HotLineItemViewSet)
router.register('category', CategoryHotLineViewSet)
router.register('subcategory', SubCategoryHotLineViewSet)
router.register('comment', HotLineCommentViewSet)
router.register('files', HotLineFileViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
