# Generated by Django 5.0.6 on 2024-07-04 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0004_alter_user_user_unique_gen_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_unique_gen_id',
            field=models.CharField(editable=False, max_length=254, unique=True),
        ),
    ]
