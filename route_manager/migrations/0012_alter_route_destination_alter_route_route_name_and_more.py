# Generated by Django 5.1.4 on 2024-12-14 10:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "route_manager",
            "0011_alter_route_destination_alter_route_route_name_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="route",
            name="destination",
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name="route",
            name="route_name",
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name="route",
            name="starting_point",
            field=models.CharField(blank=True, max_length=255),
        ),
    ]