# Generated by Django 5.1.2 on 2024-11-01 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='dislike_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='review',
            name='like_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
