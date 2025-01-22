# Generated by Django 5.1.5 on 2025-01-21 19:31

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_client', '0008_textentry_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='textentry',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='textentry',
            name='date_modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
