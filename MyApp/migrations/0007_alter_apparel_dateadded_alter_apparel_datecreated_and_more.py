# Generated by Django 4.2.3 on 2024-02-01 09:12

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0006_alter_apparel_dateadded_alter_apparel_datecreated_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apparel',
            name='DateAdded',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 1, 11, 12, 41, 729886)),
        ),
        migrations.AlterField(
            model_name='apparel',
            name='DateCreated',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 1, 11, 12, 41, 729886)),
        ),
        migrations.AlterField(
            model_name='application',
            name='ApplicationDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 1, 11, 12, 41, 729886)),
        ),
        migrations.AlterField(
            model_name='application',
            name='DateCreated',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 1, 11, 12, 41, 729886)),
        ),
        migrations.AlterField(
            model_name='federationpersonel',
            name='dateSelected',
            field=models.DateField(default=datetime.datetime(2024, 2, 1, 11, 12, 41, 729886)),
        ),
        migrations.CreateModel(
            name='Documents',
            fields=[
                ('DocumentsId', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('RegulationsInterestDeclaration', models.FileField(upload_to='MyApp/Docs')),
                ('SelectionCriteriaProtocols', models.FileField(upload_to='MyApp/Docs')),
                ('GeneralRegulationSelectionProcedure', models.FileField(upload_to='MyApp/Docs')),
                ('DocumentationOfSelectionSubmitted', models.FileField(upload_to='MyApp/Docs')),
                ('TeamOfficialDuties', models.FileField(upload_to='MyApp/Docs')),
                ('AcceptanceOfTeamAppointment', models.FileField(upload_to='MyApp/Docs')),
                ('HighPerformancePlan', models.FileField(upload_to='MyApp/Docs')),
                ('EventInvitation', models.FileField(upload_to='MyApp/Docs')),
                ('DateAdded', models.DateTimeField(default=datetime.datetime(2024, 2, 1, 11, 12, 41, 729886))),
                ('Year', models.CharField(max_length=12)),
                ('FederationPersonel', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='MyApp.federationpersonel')),
            ],
        ),
    ]