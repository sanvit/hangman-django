# Generated by Django 4.0.5 on 2022-06-28 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hangman',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=100)),
                ('tried_chars', models.CharField(blank=True, default='', max_length=26)),
                ('max_try', models.SmallIntegerField(default=7)),
            ],
        ),
    ]
