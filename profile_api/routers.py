"""Routers for the profile_api app."""
from rest_framework.routers import SimpleRouter

from profile_api.viewsets import (
    LoginViewSet,
    UserProfileViewSet,
    UserProfileFeedViewset
)


api_router = SimpleRouter()
api_router.register(
    'profile', UserProfileViewSet, basename='user-profile')
api_router.register('login', LoginViewSet, basename='login')
api_router.register(
    'feed', UserProfileFeedViewset, basename='user-profile-feed')

urlpatterns = api_router.urls
