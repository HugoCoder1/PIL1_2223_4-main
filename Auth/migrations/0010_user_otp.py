# Generated by Django 4.2.2 on 2023-06-30 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0009_alter_user_image_path'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='otp',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
