# Generated by Django 4.1.5 on 2023-11-08 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_communitymessageviewers_communitymessageviewer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='community',
            name='created_by',
            field=models.CharField(editable=False, max_length=100000, null=True),
        ),
        migrations.AlterField(
            model_name='community',
            name='created_on',
            field=models.DateTimeField(editable=False, null=True),
        ),
    ]
