# Generated by Django 4.0.6 on 2022-08-10 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Chat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mensaje',
            name='fecha_mensaje',
            field=models.DateTimeField(),
        ),
    ]
