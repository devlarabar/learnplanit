# Generated by Django 4.1.9 on 2023-10-30 13:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0004_rename_lessoncomment_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='last_updated',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
