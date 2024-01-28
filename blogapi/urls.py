from django.urls import path, include
# from rest_framework import routers
from rest_framework_nested import routers
from rest_framework.authtoken.views import obtain_auth_token
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from .views import *


router = routers.DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')

posts_router = routers.NestedSimpleRouter(router, r'posts', lookup='post')
posts_router.register(r'comments', CommentViewSet, basename='post-comments')
# router.register(r'users', UserViewSet, basename='user')



urlpatterns = [
    path('', include(router.urls)),
    path('', include(posts_router.urls)),
    path('token/', obtain_auth_token, name='api_token'),
    path('schema/docs/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]

