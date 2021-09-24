# Generated by Django 3.2.5 on 2021-09-23 14:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('departments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_score', models.IntegerField(default=0)),
                ('exam_score', models.IntegerField(default=0)),
                ('current_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='departments.stud_class')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='departments.academicsession')),
            ],
            options={
                'ordering': ['subject'],
            },
        ),
    ]
