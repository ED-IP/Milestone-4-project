# Generated by Django 3.2.5 on 2021-08-25 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0013_auto_20210825_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactform',
            name='user_username',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
