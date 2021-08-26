from django.db import models

from profiles.models import UserProfile

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=254, null=True)
    author = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    EDITIONS = [            # https://docs.djangoproject.com/en/3.2/ref/models/fields/#django.db.models.Field.choices
        ('SC', 'Soft Cover'),
        ('HC', 'Hard Cover'),
    ]
    # rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title


class WhisList(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True)
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.user_profile
