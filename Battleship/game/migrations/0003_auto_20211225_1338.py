# Generated by Django 3.2.9 on 2021-12-25 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_alter_player_avatar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='player',
            name='avatar',
            field=models.ImageField(blank=True, default='images/default.png', null=True, upload_to='images'),
        ),
    ]
