# Generated by Django 4.1.2 on 2023-08-15 14:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0015_alter_application_applicationdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='ApplicationDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 15, 16, 50, 18, 175775)),
        ),
    ]