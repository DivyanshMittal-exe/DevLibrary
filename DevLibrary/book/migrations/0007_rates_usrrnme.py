# Generated by Django 3.2 on 2021-04-21 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0006_rating_usrrnme'),
    ]

    operations = [
        migrations.AddField(
            model_name='rates',
            name='usrrnme',
            field=models.CharField(max_length=50, null=True),
        ),
    ]