# Generated by Django 5.0.7 on 2024-10-15 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0004_alter_comentario_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentario',
            name='aprobado_por_ia',
            field=models.BooleanField(default=False),
        ),
    ]
