# Generated by Django 4.0 on 2022-08-08 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='time',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='date',
            field=models.DateField(null=True),
        ),
    ]
