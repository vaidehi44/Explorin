# Generated by Django 3.1.4 on 2021-01-06 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_auto_20210107_0244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='follow',
            name='value',
            field=models.CharField(choices=[('Follow', 'Follow'), ('Following', 'Following')], max_length=10),
        ),
    ]
