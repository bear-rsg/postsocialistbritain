# Generated by Django 3.2.12 on 2022-02-25 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communities', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='author_email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AddField(
            model_name='story',
            name='author_name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='story',
            name='story_theme',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]