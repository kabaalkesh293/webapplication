# Generated by Django 3.0.4 on 2020-03-19 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empid', models.CharField(max_length=10)),
                ('empname', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=100)),
                ('contact', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'employees',
            },
        ),
    ]