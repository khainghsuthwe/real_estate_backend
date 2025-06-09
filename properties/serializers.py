from rest_framework import serializers
from .models import Property, Inquiry, Favorite, CustomUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "user_type",
            "phone",
            "bio",
            "profile_picture",
        ]


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    user_type = serializers.ChoiceField(
        choices=CustomUser.USER_TYPE_CHOICES, default="user"
    )

    class Meta:
        model = CustomUser
        fields = [
            "username",
            "email",
            "password",
            "user_type",
            "phone",
            "bio",
            "profile_picture",
        ]

    def create(self, validated_data):
        user_type = validated_data.pop("user_type")
        user = CustomUser.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
            user_type=user_type,
            phone=validated_data.get("phone", ""),
            bio=validated_data.get("bio", ""),
            profile_picture=validated_data.get("profile_picture", None),
        )
        return user


class PropertySerializer(serializers.ModelSerializer):
    agent = serializers.StringRelatedField()

    class Meta:
        model = Property
        fields = [
            "id",
            "title",
            "description",
            "price",
            "listing_type",
            "property_type",
            "address",
            "city",
            "state",
            "zip_code",
            "bedrooms",
            "bathrooms",
            "square_feet",
            "latitude",
            "longitude",
            "is_available",
            "sold_or_rented_at",
            "is_featured",
            "feature_cost",
            "amenities",
            "image_urls",
            "created_at",
            "updated_at",
            "agent",
        ]

    # If using SQLite with TextField for amenities and image_urls
    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     if isinstance(instance.amenities, str):  # For SQLite
    #         representation["amenities"] = (
    #             instance.amenities.split(",") if instance.amenities else []
    #         )
    #     if isinstance(instance.image_urls, str):  # For SQLite
    #         representation["image_urls"] = (
    #             instance.image_urls.split(",") if instance.image_urls else []
    #         )
    #     return representation

    # def to_internal_value(self, data):
    #     if isinstance(data.get("amenities"), list):  # For SQLite
    #         data["amenities"] = ",".join(data["amenities"])
    #     if isinstance(data.get("image_urls"), list):  # For SQLite
    #         data["image_urls"] = ",".join(data["image_urls"])
    #     return super().to_internal_value(data)


class InquirySerializer(serializers.ModelSerializer):
    property = serializers.StringRelatedField()

    class Meta:
        model = Inquiry
        fields = ["id", "property", "name", "email", "phone", "message", "created_at"]


class FavoriteSerializer(serializers.ModelSerializer):
    property = PropertySerializer(read_only=True)

    class Meta:
        model = Favorite
        fields = ["id", "property", "created_at"]


class AdminStatsSerializer(serializers.Serializer):
    total_users = serializers.IntegerField()
    total_properties = serializers.IntegerField()
    total_inquiries = serializers.IntegerField()
