# Generated by Django 3.2.2 on 2021-05-11 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voo',
            name='data',
            field=models.DateField(),
        ),
    ]
