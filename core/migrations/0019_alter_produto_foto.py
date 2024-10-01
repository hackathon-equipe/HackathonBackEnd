# Generated by Django 5.1.1 on 2024-09-29 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0018_produto_foto"),
        ("uploader", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="produto",
            name="foto",
            field=models.ManyToManyField(
                blank=True, default=None, null=True, related_name="produto_foto", to="uploader.image"
            ),
        ),
    ]
