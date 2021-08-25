from django.contrib import admin
from .models import ContactForm

# Register your models here.


class ContactFormAdmin(admin.ModelAdmin):

    fields = ('user', 'user_email', 'user_phone_number', 'description',)


admin.site.register(ContactForm, ContactFormAdmin)
