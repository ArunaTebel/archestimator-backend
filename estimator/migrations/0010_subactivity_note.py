# Generated by Django 2.2.2 on 2019-07-07 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estimator', '0009_remove_subactivity_estimate'),
    ]

    operations = [
        migrations.AddField(
            model_name='subactivity',
            name='note',
            field=models.TextField(max_length=10000, null=True),
        ),
    ]
