# Generated by Django 5.0.1 on 2024-02-04 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_shop', '0002_sneakers'),
    ]

    operations = [
        migrations.AddField(
            model_name='sneakers',
            name='image',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]