# Generated by Django 4.0.4 on 2022-05-18 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoreAPI', '0005_studentassignments_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentassignments',
            name='comment',
            field=models.TextField(blank=True, max_length=240),
        ),
    ]
