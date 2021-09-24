# Generated by Django 3.2.5 on 2021-09-23 14:26

import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive')], default='active', max_length=10)),
                ('first_name', models.CharField(max_length=200)),
                ('surname', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=10)),
                ('date_of_birth', models.DateField(default=django.utils.timezone.now)),
                ('date_of_admission', models.DateField(default=django.utils.timezone.now)),
                ('mobile_number', models.CharField(max_length=14, validators=[django.core.validators.RegexValidator(message='Enter a valid phone number', regex='^[0-9]{10,15}$')])),
                ('address', models.TextField()),
                ('others', models.TextField(blank=True)),
            ],
        ),
    ]
