# Generated by Django 2.1.7 on 2019-07-17 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0004_tutorial_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorialaccess',
            name='last_access',
            field=models.DateTimeField(auto_now=True, verbose_name='last accessed'),
        ),
    ]