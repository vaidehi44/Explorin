# Generated by Django 3.1.4 on 2021-01-02 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_posts_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
