# Generated by Django 4.2.2 on 2023-07-02 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0003_alter_phone_image_alter_phone_release_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
