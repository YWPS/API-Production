# Generated by Django 3.1.7 on 2021-04-14 01:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('APICore', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='full',
            field=models.CharField(default=django.utils.timezone.now, max_length=512),
            preserve_default=False,
        ),
    ]
