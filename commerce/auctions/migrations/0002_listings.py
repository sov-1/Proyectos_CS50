# Generated by Django 4.2.1 on 2023-05-26 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('bid', models.PositiveSmallIntegerField()),
                ('image', models.URLField(blank=True)),
                ('category', models.CharField(max_length=100)),
            ],
        ),
    ]
