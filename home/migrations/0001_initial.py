# Generated by Django 4.1.4 on 2023-02-03 10:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=200)),
                ('addeddate', models.DateField(auto_now=True)),
                ('about', models.TextField()),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('course', models.CharField(choices=[('ENGINEERING', 'ENGINEERING'), ('BSC', 'BSC'), ('BCOM', 'BCOM'), ('BBA', 'BBA'), ('LAW', 'LAW')], max_length=200)),
                ('mobile', models.IntegerField()),
                ('college', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.college')),
            ],
        ),
    ]
