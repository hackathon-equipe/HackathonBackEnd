# Generated by Django 5.1.1 on 2024-10-05 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0025_remove_categoria_tipo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="produto",
            name="descricao",
            field=models.JSONField(null=True),
        ),
    ]
