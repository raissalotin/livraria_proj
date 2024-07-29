# Generated by Django 5.0.2 on 2024-07-29 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0006_rename_nome_livro_titulo_livro_preco"),
    ]

    operations = [
        migrations.AddField(
            model_name="livro",
            name="isbn",
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AddField(
            model_name="livro",
            name="quantidade",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="livro",
            name="preco",
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=7, null=True),
        ),
        migrations.AlterField(
            model_name="livro",
            name="titulo",
            field=models.CharField(max_length=255),
        ),
    ]
