# Generated by Django 3.2.5 on 2023-07-06 21:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('management', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('staff', '0001_initial'),
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subjectassigntostudent',
            name='student',
            field=models.ManyToManyField(to='students.Student'),
        ),
        migrations.AddField(
            model_name='subjectassigntostudent',
            name='subject',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='management.subject'),
        ),
        migrations.AddField(
            model_name='subject',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='stud_class',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='department',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='department',
            name='head',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='staff.staff'),
        ),
        migrations.AddField(
            model_name='dailyattendance',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='students.student'),
        ),
        migrations.AddField(
            model_name='dailyattendance',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='staff.staff'),
        ),
        migrations.AddField(
            model_name='academicterm',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='academicterm',
            name='guide',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='staff.staff'),
        ),
        migrations.AddField(
            model_name='academicsession',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
