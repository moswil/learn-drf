"""Views for our profile_api app."""
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from profile_api.serializers import UserProfileSerializer, ProfileFeedItemsSerialzer
from profile_api.models import UserProfile, ProfileFeedItems
from profile_api.permissions import UpdateOwnPermission, PostOwnStatus


class UserProfileViewSet(ModelViewSet):
    """Views for the UserProfile."""

    queryset = UserProfile.objects.all().filter(
        is_deleted__exact=False)
    serializer_class = UserProfileSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (UpdateOwnPermission,)
    filter_backends = (SearchFilter,)
    search_fields = ('name', 'email',)

    @action(detail=False, permission_classes=[IsAdminUser])
    def archived(self, request, *args, **kwargs):
        """Return the deleted/archived users."""
        users = UserProfile.objects.all().filter(
            is_deleted__exact=True)

        serializer = self.get_serializer(users, many=True)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        """Override the destroy model instance.

        Archives the user, instead of deleting the user from the database.
        """
        user = self.get_object()
        user.is_deleted = True
        user.is_active = False
        user.save()

        return Response(status=HTTP_204_NO_CONTENT)


class LoginViewSet(ViewSet):
    """Checks email and password and returns an auth token."""

    queryset = UserProfile.objects.all()
    serializer_class = AuthTokenSerializer

    def create(self, request):
        """Use the ObtainAuthTokenAPI APIView to validate and create a token."""
        return ObtainAuthToken().post(request=request)


class UserProfileFeedViewset(ModelViewSet):
    """Handles CRUD of profile feed items."""

    authentication_classes = (TokenAuthentication,)
    serializer_class = ProfileFeedItemsSerialzer
    queryset = ProfileFeedItems.objects.all()
    permission_classes = (
        PostOwnStatus, IsAuthenticated,)

    def perform_create(self, serializer):
        """Set the user profile to the logged in user."""
        serializer.save(user_profile=self.request.user)
