# Generated by Django 2.2 on 2019-04-10 12:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_version'),
    ]

    operations = [
        migrations.RenameField(
            model_name='version',
            old_name='disponible',
            new_name='available',
        ),
    ]