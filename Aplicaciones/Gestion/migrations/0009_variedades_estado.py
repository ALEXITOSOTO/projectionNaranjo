# Generated by Django 5.0.6 on 2024-08-05 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gestion', '0008_variedades_ciclo_fenologico_variedades_dias_ciclo'),
    ]

    operations = [
        migrations.AddField(
            model_name='variedades',
            name='estado',
            field=models.CharField(choices=[('A', 'Activo'), ('I', 'Inactivo')], default='A', max_length=1),
        ),
    ]