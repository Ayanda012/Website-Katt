# Generated by Django 5.0.1 on 2024-02-16 18:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plans', '0004_service_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='Image',
            new_name='image',
        ),
    ]
