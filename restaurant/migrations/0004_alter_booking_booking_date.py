# Generated by Django 4.2.2 on 2023-06-30 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_alter_booking_booking_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='booking_date',
            field=models.DateTimeField(),
        ),
    ]