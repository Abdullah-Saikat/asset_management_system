# Generated by Django 4.1.4 on 2022-12-22 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0002_alter_usertype_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertype',
            name='user_type',
            field=models.CharField(choices=[('Admin', 'Admin'), ('Staff', 'Staff'), ('Store_man', 'Store_man')], default='Admin', max_length=20),
        ),
    ]
