# Generated by Django 4.2 on 2023-09-18 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Prayer_App', '0005_video_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='video_url',
        ),
        migrations.AddField(
            model_name='video',
            name='video_file',
            field=models.FileField(default=1, upload_to='videos/'),
            preserve_default=False,
        ),
    ]