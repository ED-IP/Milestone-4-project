from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_countries.fields import CountryField

# Create your models here.


class UserProfile(models.Model):
    """ User profile model for maintaining default
        delivery information and order history"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_phone_number = models.CharField(max_length=20, null=True, blank=True)
    default_street_address1 = models.CharField(max_length=80, null=True, blank=True)
    default_street_address2 = models.CharField(max_length=80, null=True, blank=True)
    default_town_or_city = models.CharField(max_length=40, null=True, blank=True)
    default_county = models.CharField(max_length=80, null=True, blank=True)
    default_postcode = models.CharField(max_length=20, null=True, blank=True)
    default_country = CountryField(blank_label="Country", null=True, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """Create or update user profile"""
    if created:
        UserProfile.objects.create(user=instance)
    # for existing user - save the profile
    instance.userprofile.save()


class ContactForm(models.Model):
    """ contact form model"""
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    # user_phone_number = models.CharField(max_length=20, null=True, blank=True)
    # user_email = models.CharField(max_length=80, null=True, blank=True)
    # description = models.TextField()
    # user_id = models.CharField(max_length=40, null=True, blank=True)

    contact_user = models.CharField(max_length=20, null=True, blank=True)
    contact_user_id = models.CharField(max_length=20, null=True, blank=True)
    contact_user_email = models.EmailField()
    conatact_user_phone_number = models.CharField(max_length=20, null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.contact_user_email
