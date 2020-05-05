"""Views for our profile_api app."""
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.decorators import action

from profile_api.serializers import UserProfileSerializer
from profile_api.models import UserProfile
from profile_api.permissions import UpdateOwnPermission


class UserProfileViewSet(ModelViewSet):
    """Views for the UserProfile."""

    queryset = UserProfile.objects.all().filter(
        is_deleted__exact=False)
    serializer_class = UserProfileSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (UpdateOwnPermission,)
    filter_backends = (SearchFilter,)
    search_fields = ('name', 'email',)

    # def list(self, request, *args, **kwargs):
    #     """Override the DRF list, to get non-deleted users."""
    #     pk = self.request.query_params.get('pk')
    #     if pk is None:
    #         users = self.queryset.filter(
    #             is_deleted__exact=False)
    #     else:
    #         users = self.queryset.get(id__exact=pk)

    #     page = self.paginate_queryset(users)
    #     if page is not None:
    #         serializer = self.get_serializer(
    #             page, many=True)
    #         return self.get_paginated_response(serializer.data)

    #     serializer = self.get_serializer(users, many=True)
    #     return Response(serializer.data)

    @action(detail=False)
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
