from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Property, Inquiry, Favorite


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ("username", "email", "user_type", "phone", "is_staff")
    list_filter = ("user_type", "is_staff")
    search_fields = ("username", "email")
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (
            "Personal info",
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "email",
                    "user_type",
                    "phone",
                    "bio",
                    "profile_picture",
                )
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "email",
                    "password1",
                    "password2",
                    "user_type",
                    "phone",
                    "bio",
                    "profile_picture",
                ),
            },
        ),
    )


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "price",
        "listing_type",
        "city",
        "agent",
        "is_available",
        "is_featured",
    )
    list_filter = (
        "city",
        "state",
        "property_type",
        "listing_type",
        "is_available",
        "is_featured",
    )
    search_fields = ("title", "description", "address")
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "title",
                    "description",
                    "price",
                    "listing_type",
                    "property_type",
                    "agent",
                    "is_available",
                )
            },
        ),
        (
            "Location",
            {
                "fields": (
                    "address",
                    "city",
                    "state",
                    "zip_code",
                    "latitude",
                    "longitude",
                )
            },
        ),
        (
            "Details",
            {
                "fields": (
                    "bedrooms",
                    "bathrooms",
                    "square_feet",
                    "amenities",
                    "image_urls",
                )
            },
        ),
        ("Featured", {"fields": ("is_featured", "feature_cost")}),
        ("Status", {"fields": ("sold_or_rented_at", "created_at", "updated_at")}),
    )


@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = ("name", "property", "email", "created_at")
    list_filter = ("property", "created_at")
    search_fields = ("name", "email")


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ("user", "property", "created_at")
    list_filter = ("user", "property")
