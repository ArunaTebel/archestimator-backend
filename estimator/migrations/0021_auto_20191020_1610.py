# Generated by Django 2.2.2 on 2019-10-20 16:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('estimator', '0020_auto_20191020_1603'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='estimator.Resource'),
        ),
        migrations.AddField(
            model_name='subactivity',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='estimator.Resource'),
        ),
    ]
