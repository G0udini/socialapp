# Generated by Django 3.2.6 on 2021-09-04 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0002_rename_creaeted_image_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='total_likes',
            field=models.PositiveIntegerField(db_index=True, default=0),
        ),
    ]
