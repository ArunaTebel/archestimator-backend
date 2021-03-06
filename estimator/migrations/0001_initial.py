# Generated by Django 2.2.2 on 2019-06-15 13:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=2000)),
                ('estimated_time', models.IntegerField()),
                ('is_completed', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Estimate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='SubActivity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estimated_time', models.IntegerField()),
                ('is_completed', models.BooleanField()),
                ('estimate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estimator.Estimate')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estimator.Activity')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=200)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='estimator.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Phase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estimator.Customer')),
                ('resources', models.ManyToManyField(to='estimator.Resource')),
            ],
        ),
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('phase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estimator.Phase')),
            ],
        ),
        migrations.AddField(
            model_name='estimate',
            name='feature',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estimator.Feature'),
        ),
        migrations.AddField(
            model_name='estimate',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estimator.Resource'),
        ),
        migrations.AddField(
            model_name='activity',
            name='estimate',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estimator.Estimate'),
        ),
    ]
