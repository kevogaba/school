# Generated by Django 3.2.5 on 2021-09-24 11:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
        ('management', '0003_auto_20210924_1111'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('results', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='result',
            unique_together={('subject', 'student')},
        ),
    ]