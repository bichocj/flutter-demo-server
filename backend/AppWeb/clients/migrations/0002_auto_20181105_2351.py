# Generated by Django 2.0.2 on 2018-11-06 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='last_lat',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='client',
            name='last_lon',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
