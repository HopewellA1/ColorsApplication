# Generated by Django 4.2.3 on 2023-08-11 08:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0008_committeemember_teamofficial_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='RepresatativeType',
        ),
        migrations.AddField(
            model_name='represantative',
            name='RepresatativeType',
            field=models.CharField(default='Junior', max_length=255),
        ),
        migrations.AlterField(
            model_name='application',
            name='ApplicationDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 11, 10, 0, 37, 205767)),
        ),
    ]