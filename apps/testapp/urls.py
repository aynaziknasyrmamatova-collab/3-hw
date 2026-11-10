from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from apps.testapp.views import (
    LogoutView,
    ProfileStatsView,
    UserTokenObtainPairView,
)

urlpatterns = [
    path("token/", UserTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("profile/stats/", ProfileStatsView.as_view(), name="profile_stats"),
]