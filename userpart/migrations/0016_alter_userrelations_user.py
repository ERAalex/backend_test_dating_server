# Generated by Django 4.2.2 on 2023-06-30 14:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userpart', '0015_useraccount_latitude_useraccount_longitude'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userrelations',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
