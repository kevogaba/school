# Generated by Django 3.2.5 on 2021-09-23 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academicsession',
            name='current',
            field=models.BooleanField(default=True),
        ),
    ]
