# Generated by Django 3.1.4 on 2021-01-09 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_auto_20210108_0456'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comments',
            options={'ordering': ['-date']},
        ),
        migrations.AlterField(
            model_name='posts',
            name='image',
            field=models.ImageField(blank=True, default='images/default_user_pic.svg', null=True, upload_to='images/'),
        ),
    ]