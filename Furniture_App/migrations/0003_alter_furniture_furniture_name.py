# Generated by Django 4.2.9 on 2024-01-19 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Furniture_App", "0002_alter_furniture_furniture_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="furniture",
            name="furniture_name",
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
