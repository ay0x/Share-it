# Generated by Django 5.0.6 on 2024-07-06 11:19

import datetime
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0015_alter_uploadfile_expiration_date_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadfile',
            name='expiration_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 7, 11, 19, 16, 884694, tzinfo=datetime.timezone.utc)),
        ),
        migrations.CreateModel(
            name='DeletedFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=255)),
                ('file_size', models.PositiveBigIntegerField()),
                ('upload_date', models.DateTimeField()),
                ('deletion_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('upload_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
