# Generated by Django 2.2.2 on 2019-07-07 09:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estimator', '0008_estimate_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subactivity',
            name='estimate',
        ),
    ]
