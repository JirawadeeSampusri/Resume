# Generated by Django 2.2.6 on 2021-01-21 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(default=None, upload_to='upload/')),
                ('first_name', models.CharField(default='', max_length=254, verbose_name='First Name')),
                ('last_name', models.CharField(default='', max_length=254, verbose_name='Last Name')),
                ('gender', models.CharField(default='', max_length=254, verbose_name='Gender')),
                ('nationality', models.CharField(default='', max_length=254, verbose_name='Nationality')),
                ('interest', models.TextField(default='', max_length=300, verbose_name='Interest')),
                ('branch', models.CharField(default='', max_length=254, verbose_name='Branch')),
                ('skill', models.TextField(default='', max_length=300, verbose_name='Skill')),
                ('email', models.EmailField(default='', max_length=254, verbose_name='E-mail')),
                ('tel', models.CharField(default='', max_length=254, verbose_name='Tel')),
                ('gpa', models.CharField(default='', max_length=254, verbose_name='GPA')),
                ('address', models.TextField(default='', max_length=200, verbose_name='Address')),
                ('short_description', models.TextField(default='', max_length=300, verbose_name='Short Description')),
                ('university', models.CharField(default='', max_length=80, verbose_name='University')),
                ('bachelor', models.CharField(default='', max_length=80, verbose_name='Bachelor')),
                ('major', models.CharField(default='', max_length=80, verbose_name='Major')),
                ('start_study', models.DateTimeField(default='YYYY-MM-DD [:ss[.uuuuuu]][TZ]', verbose_name='Start Date')),
                ('end_study', models.DateTimeField(default='YYYY-MM-DD [:ss[.uuuuuu]][TZ]', verbose_name='End Date')),
                ('birth', models.DateTimeField(default='YYYY-MM-DD [:ss[.uuuuuu]][TZ]', verbose_name='Birth')),
            ],
        ),
    ]
