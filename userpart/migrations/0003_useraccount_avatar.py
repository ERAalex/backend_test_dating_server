# Generated by Django 4.2.2 on 2023-06-29 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userpart', '0002_useraccount_sex'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]