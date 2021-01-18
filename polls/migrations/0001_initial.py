# Generated by Django 2.2.6 on 2021-01-17 13:10

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('university', models.TextField(default='', max_length=80, verbose_name='University')),
                ('bachelor', models.TextField(default='', max_length=80, verbose_name='Bachelor')),
                ('major', models.TextField(default='', max_length=80, verbose_name='Major')),
                ('start_study', models.DateTimeField(default=datetime.datetime(2021, 1, 17, 13, 10, 48, 614644, tzinfo=utc), verbose_name='Start Date')),
                ('end_study', models.DateTimeField(default=datetime.datetime(2021, 1, 17, 13, 10, 48, 614691, tzinfo=utc), verbose_name='End Date')),
            ],
        ),
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(default=None, upload_to='upload/')),
                ('first_name', models.CharField(default='', max_length=254, verbose_name='First Name')),
                ('last_name', models.CharField(default='', max_length=254, verbose_name='Last Name')),
                ('gender', models.CharField(default='', max_length=254, verbose_name='Gender')),
                ('nationality', models.CharField(default='', max_length=254, verbose_name='Nationality')),
                ('interest', models.CharField(default='', max_length=100, verbose_name='Interest')),
                ('email', models.EmailField(default='', max_length=254, verbose_name='E-mail')),
                ('address', models.CharField(default='', max_length=125, verbose_name='Address')),
                ('short_description', models.CharField(default='', max_length=100, verbose_name='Short Description')),
            ],
        ),
    ]