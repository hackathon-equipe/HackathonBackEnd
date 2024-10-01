# Generated by Django 5.0.6 on 2024-09-24 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0007_fabricante_cnpj_fabricante_email_fabricante_site"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="produto",
            name="fabricante",
        ),
        migrations.AddField(
            model_name="produto",
            name="descricao",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="produto",
            name="fabricantes",
            field=models.ManyToManyField(blank=True, related_name="produto_fabricante", to="core.fabricante"),
        ),
        migrations.AddField(
            model_name="produto",
            name="garantia_meses",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name="produto",
            name="preco",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=7),
        ),
    ]
