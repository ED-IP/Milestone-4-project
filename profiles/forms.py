from django import forms
from .models import UserProfile, ContactForm


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """ Add place holders and classes, remove auto-generated labels and set autofocus on firest field"""

        super().__init__(*args, **kwargs)
        placeholders = {
            'default_phone_number': 'Phone Numer',
            'default_postcode': 'Postal Code',
            'default_town_or_city': 'Town or City',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_county': 'County, State or Locality',
        }

        self.fields['default_phone_number'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'default_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-black rounded-0 profile-form-input'
            self.fields[field].label = False


class UserContactForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = [
            'user_username',
            'user_email',
            'user_phone_number',
            'description',
        ]
