# Generated by Django 3.0.6 on 2020-05-09 17:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('first_api', '0002_album_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='skills', to=settings.AUTH_USER_MODEL),
        ),
    ]
