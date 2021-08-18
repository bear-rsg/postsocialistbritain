# Generated by Django 3.2.6 on 2021-08-10 18:41

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Output',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='outputs-images')),
                ('file', models.FileField(blank=True, null=True, upload_to='outputs-files')),
                ('link', models.URLField(blank=True, null=True)),
                ('admin_published', models.BooleanField(default=False)),
                ('admin_notes', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('meta_created_datetime', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('meta_lastupdated_datetime', models.DateTimeField(auto_now=True, verbose_name='Last Updated')),
            ],
            options={
                'ordering': ['name', '-id'],
            },
        ),
    ]
