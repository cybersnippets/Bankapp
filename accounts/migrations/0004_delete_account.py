# Generated by Django 5.0.4 on 2024-06-26 07:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_profile_user_alter_userbankaccount_user_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Account',
        ),
    ]
