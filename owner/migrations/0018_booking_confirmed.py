# Generated by Django 5.0.6 on 2024-07-20 15:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("owner", "0017_venue_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="booking",
            name="confirmed",
            field=models.BooleanField(default=False),
        ),
    ]