# Generated by Django 2.2 on 2019-04-11 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_version_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='version',
            name='code',
            field=models.CharField(max_length=7, unique=True),
        ),
    ]