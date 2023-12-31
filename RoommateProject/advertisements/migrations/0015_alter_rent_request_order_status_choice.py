# Generated by Django 5.0 on 2023-12-26 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements', '0014_rename_order_status_rent_request_order_status_choice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rent_request',
            name='order_status_choice',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Denied', 'Denied'), ('Finish', 'Finish')], default='Pending', max_length=500),
        ),
    ]
