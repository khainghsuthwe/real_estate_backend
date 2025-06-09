from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import (
    PropertyViewSet,
    InquiryViewSet,
    RegisterView,
    UserView,
    FavoriteView,
    RemoveFavoriteView,
    AdminUserViewSet,
    AdminPropertyViewSet,
    AdminStatsView,
)

router = DefaultRouter()
router.register(r"properties", PropertyViewSet, basename="property")
router.register(r"inquiries", InquiryViewSet, basename="inquiry")
router.register(r"admin/users", AdminUserViewSet, basename="admin_user")
router.register(r"admin/properties", AdminPropertyViewSet, basename="admin_property")

urlpatterns = [
    path("", include(router.urls)),
    path("register/", RegisterView.as_view(), name="register"),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("user/", UserView.as_view(), name="user_details"),
    path(
        "user/add-favorite/<int:property_id>/",
        FavoriteView.as_view(),
        name="add_favorite",
    ),
    path(
        "user/remove-favorite/<int:property_id>/",
        RemoveFavoriteView.as_view(),
        name="remove_favorite",
    ),
    path("admin/stats/", AdminStatsView.as_view(), name="admin_stats"),
]
