# Generated by Django 5.0.2 on 2024-07-29 14:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0007_livro_isbn_livro_quantidade_alter_livro_preco_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="livro",
            name="categoria",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="livros",
                to="core.categoria",
            ),
        ),
        migrations.AddField(
            model_name="livro",
            name="editora",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="livros",
                to="core.editora",
            ),
        ),
    ]
