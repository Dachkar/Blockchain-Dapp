# Generated by Django 2.1.7 on 2019-02-18 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_remove_store_date_posted'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='money',
            field=models.DecimalField(decimal_places=2, default=500, max_digits=8),
        ),
    ]
