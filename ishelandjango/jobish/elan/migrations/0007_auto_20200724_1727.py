# Generated by Django 3.0.8 on 2020-07-24 13:27

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elan', '0006_elan_image_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elan',
            name='job_description',
            field=ckeditor.fields.RichTextField(null=True),
        ),
    ]
