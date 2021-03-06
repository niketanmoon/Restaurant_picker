# Generated by Django 2.2.5 on 2019-09-19 11:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0006_restaurantlocation_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurantlocation',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='restaurant_records', to=settings.AUTH_USER_MODEL),
        ),
    ]
