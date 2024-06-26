# Generated by Django 4.2.4 on 2024-03-25 01:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eventapp', '0069_remove_questionnaire_webinar_delete_question_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('webinar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eventapp.webinar')),
            ],
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('response', models.TextField(null=True)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eventapp.question')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eventapp.attendee')),
            ],
        ),
    ]
