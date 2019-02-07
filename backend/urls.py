from rest_framework import routers
from .api import PostViewSet, CommentViewSet

router = routers.DefaultRouter()
router.register('api/posts', PostViewSet, 'posts')
router.register('api/comments', CommentViewSet, 'comments')

urlpatterns = router.urls

# # Wire up our API using automatic URL routing.
# # Additionally, we include login URLs for the browsable API.
# urlpatterns = [
#     path('', include(router.urls)),
#     path('api-auth/', include('backend.urls', namespace='backend'))
#     # path('api-auth/', include('backend.urls', namespace='rest_framework'))
# ]
