# Generated by Django 4.2.1 on 2023-07-11 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0008_alter_bids_listing_alter_bids_owner_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
