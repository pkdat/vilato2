# Generated by Django 4.1.10 on 2023-09-04 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_rename_is_active_comment_is_report'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
