from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenBlacklistView, TokenObtainPairView


class UserTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        data.update(
            {
                "id": self.user.pk,
                "email": self.user.email,
                "username": self.user.get_username(),
                "role": getattr(self.user, "role", None),
            }
        )
        return data


class UserTokenObtainPairView(TokenObtainPairView):
    serializer_class = UserTokenObtainPairSerializer


class LogoutView(TokenBlacklistView):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)


class ProfileStatsView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        user = request.user
        return Response(
            {
                "email": user.email,
                "role": getattr(user, "role", None),
                "is_staff": user.is_staff,
                "date_joined": user.date_joined,
            }
        )
