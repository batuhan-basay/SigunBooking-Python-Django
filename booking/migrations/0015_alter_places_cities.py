# Generated by Django 4.1.7 on 2023-03-26 14:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0014_places_cities'),
    ]

    operations = [
        migrations.AlterField(
            model_name='places',
            name='cities',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.cities'),
        ),
    ]
