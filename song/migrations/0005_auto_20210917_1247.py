# Generated by Django 3.2.7 on 2021-09-17 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('song', '0004_auto_20210917_1238'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='song',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
