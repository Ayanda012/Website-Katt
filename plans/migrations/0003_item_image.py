# Generated by Django 4.2.5 on 2024-02-15 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plans', '0002_remove_quotation_package_remove_item_package_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='item_images/'),
        ),
    ]