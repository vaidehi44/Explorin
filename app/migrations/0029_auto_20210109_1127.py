# Generated by Django 3.1.4 on 2021-01-09 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0028_auto_20210109_1040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='images/profile_pics/default_profile_pic.png', null=True, upload_to='images/profile_pics'),
        ),
    ]