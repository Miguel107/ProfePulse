# Generated by Django 5.0.7 on 2024-08-10 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('departamento', models.CharField(max_length=100)),
                ('materia', models.CharField(max_length=100)),
                ('calificacion_media', models.FloatField(default=0.0)),
            ],
        ),
    ]
