# Generated by Django 5.1.1 on 2024-11-24 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='members',
            name='profile_picture',
            field=models.ImageField(blank=True, default='images/default_profile_picture.jpg', null=True, upload_to='profile_pics/'),
        ),
    ]