# Generated by Django 4.2.1 on 2023-05-27 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_listings'),
    ]

    operations = [
        migrations.AddField(
            model_name='listings',
            name='dateCreated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]