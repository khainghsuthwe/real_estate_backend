from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField


class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ("user", "User"),
        ("agent", "Agent"),
        ("admin", "Admin"),
    )
    user_type = models.CharField(
        max_length=10, choices=USER_TYPE_CHOICES, default="user"
    )
    phone = models.CharField(max_length=15, blank=True)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to="users/", blank=True, null=True)

    def __str__(self):
        return self.username


class Property(models.Model):
    LISTING_TYPES = (
        ("sell", "Sell"),
        ("rent", "Rent"),
    )
    PROPERTY_TYPES = (
        ("house", "House"),
        ("apartment", "Apartment"),
        ("condo", "Condo"),
        ("land", "Land"),
    )
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    listing_type = models.CharField(
        max_length=10, choices=LISTING_TYPES, default="sell"
    )
    property_type = models.CharField(max_length=20, choices=PROPERTY_TYPES)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20, blank=True, null=True)
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    square_feet = models.IntegerField()
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    is_available = models.BooleanField(default=True)
    sold_or_rented_at = models.DateTimeField(blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    feature_cost = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True
    )
    amenities = ArrayField(models.CharField(max_length=50), blank=True, default=list)
    image_urls = ArrayField(models.URLField(max_length=200), blank=True, default=list)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    agent = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="properties",
        limit_choices_to={"user_type": "agent"},
    )

    def __str__(self):
        return self.title


class Inquiry(models.Model):
    property = models.ForeignKey(
        Property, on_delete=models.CASCADE, related_name="inquiries"
    )
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Inquiry for {self.property.title} by {self.name}"


class Favorite(models.Model):
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="favorites"
    )
    property = models.ForeignKey(
        Property, on_delete=models.CASCADE, related_name="favorited_by"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "property")

    def __str__(self):
        return f"{self.user.username} favorited {self.property.title}"
