# Generated by Django 3.2.9 on 2021-12-21 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='mobile_number',
            field=models.CharField(max_length=10),
        ),
    ]
