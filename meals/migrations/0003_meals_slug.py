# Generated by Django 4.0 on 2022-07-07 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0002_alter_meals_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='meals',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
