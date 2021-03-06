# Generated by Django 3.1.4 on 2021-01-06 14:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0013_auto_20210105_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(choices=[('Like', 'Like'), ('Unlike', 'Unlike')], max_length=8)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.posts')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
