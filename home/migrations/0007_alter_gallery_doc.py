# Generated by Django 3.2.1 on 2021-05-23 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_gallery_flag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='doc',
            field=models.FileField(default='', upload_to='docs'),
        ),
    ]
