# Generated by Django 4.2.4 on 2024-03-19 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventapp', '0062_participationcertificate'),
    ]

    operations = [
        migrations.AddField(
            model_name='participationcertificate',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='participationcertificate',
            name='organization',
            field=models.CharField(max_length=100, null=True),
        ),
    ]