# Generated by Django 5.1.1 on 2024-12-01 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard_app', '0009_delete_attendance'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='completion_status',
            field=models.BooleanField(default=False),
        ),
    ]
