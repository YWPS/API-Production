# Generated by Django 3.1.7 on 2021-03-28 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('extension', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('code1name', models.CharField(max_length=256)),
                ('code2name', models.CharField(max_length=256)),
                ('code3name', models.CharField(max_length=256)),
                ('code1code', models.CharField(max_length=256)),
                ('code2code', models.CharField(max_length=256)),
                ('code3code', models.CharField(max_length=256)),
                ('hash', models.CharField(max_length=45)),
                ('user', models.CharField(max_length=256)),
            ],
        ),
    ]
