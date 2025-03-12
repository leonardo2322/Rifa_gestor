# Generated by Django 5.1.7 on 2025-03-07 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='estado',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='nombre',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
