# Generated by Django 4.2.5 on 2023-09-22 00:28

import app_user.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_picture',
            field=models.ImageField(default='/profile_pics/temp_pfp_placeholder_REPLACE_LATER.avif', upload_to=app_user.models.generate_image_path),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='this_user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
