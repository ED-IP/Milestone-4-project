# Generated by Django 3.2.5 on 2021-08-21 11:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_contactform'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactform',
            old_name='conatact_user_phone_number',
            new_name='contact_user_phone_number',
        ),
    ]