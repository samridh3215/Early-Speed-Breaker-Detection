# Generated by Django 5.0.3 on 2024-03-15 17:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Devices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=16, verbose_name='Device Ip')),
                ('connectionDate', models.DateField(verbose_name=datetime.date)),
                ('connectionTime', models.TimeField(verbose_name=datetime.time)),
            ],
        ),
    ]
