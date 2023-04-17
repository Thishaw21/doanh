# Generated by Django 3.0.7 on 2020-09-27 10:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hotel_app', '0012_auto_20200914_1929'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkin',
            name='check_in_date',
        ),
        migrations.AddField(
            model_name='checkin',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='checkin',
            name='phone_number',
            field=models.CharField(max_length=14, null=True),
        ),
        migrations.AddField(
            model_name='checkin',
            name='room',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='hotel_app.Room'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='checkin',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
