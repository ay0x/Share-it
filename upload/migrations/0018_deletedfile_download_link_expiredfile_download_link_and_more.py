# Generated by Django 5.0.6 on 2024-07-07 07:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0017_alter_uploadfile_expiration_date_expiredfile'),
    ]

    operations = [
        migrations.AddField(
            model_name='deletedfile',
            name='download_link',
            field=models.CharField(default='V0Y4g3!', editable=False, max_length=7),
        ),
        migrations.AddField(
            model_name='expiredfile',
            name='download_link',
            field=models.CharField(default='voYage!', editable=False, max_length=7),
        ),
        migrations.AlterField(
            model_name='uploadfile',
            name='expiration_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 8, 7, 49, 9, 673328, tzinfo=datetime.timezone.utc)),
        ),
    ]