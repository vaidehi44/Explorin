# Generated by Django 3.1.4 on 2021-01-09 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0025_auto_20210109_0950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='images/profile_pics/default_user_pic.png', null=True, upload_to='images/profile_pics'),
        ),
    ]
