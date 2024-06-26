# Generated by Django 4.2.4 on 2023-09-28 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventapp', '0020_remove_webinar_time_webinar_end_time_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=255)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('interests', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
