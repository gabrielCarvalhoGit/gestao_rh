# Generated by Django 5.0.4 on 2024-06-20 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro_horas_extras', '0003_registrohoraextra_horas'),
    ]

    operations = [
        migrations.AddField(
            model_name='registrohoraextra',
            name='horas_utilizadas',
            field=models.BooleanField(default=False),
        ),
    ]