# Generated by Django 4.2.8 on 2024-07-29 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='cargo',
            field=models.CharField(blank=True, choices=[('vendedor', 'Vendedor'), ('caixa', 'Caixa'), ('administrador', 'Administrador')], max_length=20, null=True),
        ),
    ]
