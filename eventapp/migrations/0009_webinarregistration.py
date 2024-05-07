# Generated by Django 4.2.4 on 2023-09-16 04:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eventapp', '0008_customuser_is_verified_customuser_verification_token'),
    ]

    operations = [
        migrations.CreateModel(
            name='WebinarRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('webinar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eventapp.webinar')),
            ],
        ),
    ]
