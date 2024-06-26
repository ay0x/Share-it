# Generated by Django 5.0.6 on 2024-07-01 15:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0008_alter_uploadfile_download_link_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadfile',
            name='download_link',
            field=models.CharField(editable=False, max_length=7, unique=True),
        ),
        migrations.AlterField(
            model_name='uploadfile',
            name='expiration_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 2, 15, 20, 33, 660349, tzinfo=datetime.timezone.utc)),
        ),
    ]
