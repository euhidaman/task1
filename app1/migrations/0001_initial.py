# Generated by Django 3.1.2 on 2020-11-29 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idnum', models.CharField(max_length=13)),
                ('name', models.CharField(max_length=25)),
                ('branch', models.CharField(max_length=5)),
                ('gender', models.CharField(max_length=6)),
                ('dob', models.DateField()),
                ('age', models.IntegerField()),
            ],
        ),
    ]
