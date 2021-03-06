# Generated by Django 2.2.5 on 2019-09-19 10:40

from django.db import migrations, models
import restaurants.validators


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0004_restaurantlocation_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurantlocation',
            name='category',
            field=models.CharField(blank=True, max_length=120, null=True, validators=[restaurants.validators.validate_category]),
        ),
    ]
