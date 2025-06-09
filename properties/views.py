from rest_framework import viewsets, filters, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from .models import Property, Inquiry, Favorite, CustomUser
from .serializers import (
    PropertySerializer,
    InquirySerializer,
    UserSerializer,
    RegisterSerializer,
    FavoriteSerializer,
    AdminStatsSerializer,
)
from .permissions import IsAdminOrAgent, IsAdmin
from django.db.models import Count


class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)


class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = [
        "city",
        "state",
        "property_type",
        "price",
        "bedrooms",
        "bathrooms",
        "listing_type",
        "is_featured",
    ]
    search_fields = ["title", "description", "address", "city", "state"]

    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [IsAdminOrAgent()]
        return [AllowAny()]

    def perform_create(self, serializer):
        serializer.save(agent=self.request.user)


class InquiryViewSet(viewsets.ModelViewSet):
    queryset = Inquiry.objects.all()
    serializer_class = InquirySerializer
    permission_classes = [AllowAny]


class FavoriteView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, property_id):
        try:
            property = Property.objects.get(id=property_id)
            favorite, created = Favorite.objects.get_or_create(
                user=request.user, property=property
            )
            if created:
                return Response(
                    {"message": "Property added to favorites"},
                    status=status.HTTP_201_CREATED,
                )
            return Response(
                {"message": "Property already in favorites"}, status=status.HTTP_200_OK
            )
        except Property.DoesNotExist:
            return Response(
                {"error": "Property not found"}, status=status.HTTP_404_NOT_FOUND
            )


class RemoveFavoriteView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, property_id):
        try:
            favorite = Favorite.objects.get(user=request.user, property_id=property_id)
            favorite.delete()
            return Response(
                {"message": "Property removed from favorites"},
                status=status.HTTP_200_OK,
            )
        except Favorite.DoesNotExist:
            return Response(
                {"error": "Favorite not found"}, status=status.HTTP_404_NOT_FOUND
            )


class AdminUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdmin]


class AdminPropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [IsAdmin]


class AdminStatsView(APIView):
    permission_classes = [IsAdmin]

    def get(self, request):
        data = {
            "total_users": CustomUser.objects.count(),
            "total_properties": Property.objects.count(),
            "total_inquiries": Inquiry.objects.count(),
        }
        serializer = AdminStatsSerializer(data)
        return Response(serializer.data)
