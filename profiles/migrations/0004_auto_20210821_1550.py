# Generated by Django 3.2.5 on 2021-08-21 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_rename_conatact_user_phone_number_contactform_contact_user_phone_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactform',
            old_name='contact_user',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='contactform',
            old_name='contact_user_email',
            new_name='user_email',
        ),
        migrations.RenameField(
            model_name='contactform',
            old_name='contact_user_id',
            new_name='user_phone_number',
        ),
        migrations.RenameField(
            model_name='contactform',
            old_name='contact_user_phone_number',
            new_name='userid',
        ),
    ]