"""Serializers for the profile_api app."""
from rest_framework.serializers import ModelSerializer

from profile_api.models import UserProfile, ProfileFeedItems


class UserProfileSerializer(ModelSerializer):
    """Serializer class to handle UserProfile model."""

    class Meta:
        model = UserProfile
        fields = ('id', 'name', 'email',
                  'password', 'is_staff', 'is_active', 'is_deleted',)
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    def create(self, validated_data):
        """Create and return a new user."""
        user = UserProfile(
            email=validated_data['email'],
            name=validated_data['name']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user


class ProfileFeedItemsSerialzer(ModelSerializer):
    """Serializes profile feed items."""

    class Meta:
        model = ProfileFeedItems
        fields = '__all__'
        extra_kwargs = {
            'user_profile': {
                'read_only': True
            }
        }
