# Generated by Django 2.2.20 on 2023-06-20 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0090_challenge_allow_resuming_submissions'),
    ]

    operations = [
        migrations.AddField(
            model_name='challenge',
            name='allow_host_cancel_submissions',
            field=models.BooleanField(default=False),
        ),
    ]