# Generated by Django 3.0.7 on 2020-09-12 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel_app', '0010_auto_20200912_1313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='booking_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
