# Generated by Django 3.2.6 on 2021-08-29 19:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='creaeted',
            new_name='created',
        ),
    ]
