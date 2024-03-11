# Generated by Django 5.0.2 on 2024-03-11 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_categoria"),
    ]

    operations = [
        migrations.CreateModel(
            name="Editora",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("nome", models.CharField(max_length=100)),
                ("site", models.URLField(blank=True, null=True)),
            ],
        ),
    ]
