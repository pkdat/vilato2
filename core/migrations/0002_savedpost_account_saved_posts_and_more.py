# Generated by Django 4.1.10 on 2023-08-18 03:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SavedPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='acount_set', to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_set', to='core.post')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.AddField(
            model_name='account',
            name='saved_posts',
            field=models.ManyToManyField(related_name='saved_by_set', through='core.SavedPost', to='core.post'),
        ),
        migrations.AddIndex(
            model_name='savedpost',
            index=models.Index(fields=['-created_at'], name='core_savedp_created_988971_idx'),
        ),
    ]