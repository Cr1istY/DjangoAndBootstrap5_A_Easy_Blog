# Generated by Django 5.2rc1 on 2025-04-04 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Wisdom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=100)),
                ('sentence', models.CharField(max_length=100)),
                ('article', models.CharField(max_length=100)),
            ],
        ),
    ]
