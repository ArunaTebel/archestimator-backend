# Generated by Django 2.2.2 on 2019-08-10 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estimator', '0011_auto_20190810_0458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subactivity',
            name='estimated_time',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='subactivity',
            name='is_completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='subactivity',
            name='name',
            field=models.CharField(default='', max_length=2000),
        ),
    ]