# Generated by Django 2.1.4 on 2019-02-25 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0003_challenge_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='challenge',
            name='published',
            field=models.BooleanField(default=True),
        ),
    ]
