# Generated by Django 5.1.1 on 2024-09-07 23:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recomendaciones', '0002_alter_ubicacion_direccion_alter_direccion_table_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personavulnerable',
            name='direccion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recomendaciones.ubicacion'),
        ),
    ]
