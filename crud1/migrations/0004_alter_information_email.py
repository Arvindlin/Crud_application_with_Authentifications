# Generated by Django 4.0 on 2021-12-24 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud1', '0003_information_firstname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='information',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
