# Generated by Django 3.2.1 on 2021-05-23 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_gallery'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='doc',
            field=models.FileField(default='', upload_to=None),
        ),
    ]