# Generated by Django 5.0.4 on 2024-10-23 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_remove_employee_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='address',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]