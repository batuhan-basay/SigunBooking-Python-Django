# Generated by Django 4.1.7 on 2023-02-28 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0009_alter_places_cover_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='image',
            field=models.ImageField(upload_to='blogs'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='image',
            field=models.ImageField(upload_to='comments'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='image',
            field=models.ImageField(upload_to='menu'),
        ),
        migrations.AlterField(
            model_name='place_img',
            name='image',
            field=models.ImageField(upload_to='place_images'),
        ),
        migrations.AlterField(
            model_name='places',
            name='cover_img',
            field=models.ImageField(upload_to='places'),
        ),
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(upload_to='user'),
        ),
    ]