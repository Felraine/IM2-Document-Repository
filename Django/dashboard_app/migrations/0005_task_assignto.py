# Generated by Django 5.1.1 on 2024-11-28 04:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard_app', '0004_task_tasktitle_alter_task_table'),
        ('register_app', '0004_alter_members_profile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='assignTo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='task', to='register_app.members'),
        ),
    ]
