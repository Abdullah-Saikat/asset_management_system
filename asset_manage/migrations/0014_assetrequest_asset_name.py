# Generated by Django 4.1.4 on 2023-01-14 17:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asset_manage', '0013_remove_assetrequest_request_message_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='assetrequest',
            name='asset_name',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='asset_manage.asset'),
        ),
    ]
