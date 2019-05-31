# Generated by Django 2.2.1 on 2019-05-30 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('role', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('update_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
