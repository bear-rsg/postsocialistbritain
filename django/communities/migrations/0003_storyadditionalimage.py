# Generated by Django 3.2.16 on 2022-11-21 11:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('communities', '0002_auto_20220225_1549'),
    ]

    operations = [
        migrations.CreateModel(
            name='StoryAdditionalImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='communities-stories-images')),
                ('story', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='additionalimages', to='communities.story')),
            ],
        ),
    ]