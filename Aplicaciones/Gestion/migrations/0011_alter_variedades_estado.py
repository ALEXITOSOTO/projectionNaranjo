# Generated by Django 5.0.6 on 2024-08-05 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gestion', '0010_alter_variedades_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variedades',
            name='estado',
            field=models.CharField(choices=[('A', 'Activo'), ('I', 'Inactivo')], default='Activo', max_length=250),
        ),
    ]
