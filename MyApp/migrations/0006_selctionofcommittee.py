# Generated by Django 4.2.3 on 2023-07-21 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0005_alter_represantative_represantativeid'),
    ]

    operations = [
        migrations.CreateModel(
            name='SelctionOfCommittee',
            fields=[
                ('MemberId', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=255)),
                ('Surname', models.CharField(max_length=255)),
                ('Gender', models.CharField(max_length=255)),
            ],
        ),
    ]