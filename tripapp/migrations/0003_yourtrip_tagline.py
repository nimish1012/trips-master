# Generated by Django 4.2.1 on 2023-06-05 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tripapp', '0002_yourtrip'),
    ]

    operations = [
        migrations.AddField(
            model_name='yourtrip',
            name='tagline',
            field=models.TextField(blank=True, null=True),
        ),
    ]
