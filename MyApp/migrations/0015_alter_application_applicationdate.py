# Generated by Django 4.1.2 on 2023-08-15 14:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0014_rename_memberid_committeemember_committeememberid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='ApplicationDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 15, 16, 49, 3, 737342)),
        ),
    ]