# Generated by Django 5.0.4 on 2024-10-23 13:13

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_remove_employeeassignment_notes_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('attended', models.BooleanField(default=False)),
                ('day_salary', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('employee_assignment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attendances', to='home.employeeassignment')),
            ],
            options={
                'ordering': ['-date'],
                'unique_together': {('employee_assignment', 'date')},
            },
        ),
    ]