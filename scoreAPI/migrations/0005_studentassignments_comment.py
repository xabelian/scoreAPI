# Generated by Django 4.0.4 on 2022-05-18 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoreAPI', '0004_alter_studentassignments_upload_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentassignments',
            name='comment',
            field=models.TextField(blank=True, max_length=24),
        ),
    ]
