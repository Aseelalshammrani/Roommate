# Generated by Django 5.0 on 2023-12-22 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('image', models.ImageField(upload_to='images/')),
                ('type_of_duration', models.CharField(choices=[('Days', 'Days'), ('Weeks', 'Weeks'), ('Months', 'Months')], max_length=500)),
                ('duration_residence', models.IntegerField()),
                ('advertisement_date', models.DateTimeField(auto_now_add=True)),
                ('type_of_residential', models.CharField(choices=[('Apartment', 'Apartment'), ('Room', 'Room'), ('House', 'House')], max_length=500)),
                ('longitude', models.DecimalField(decimal_places=9, max_digits=12)),
                ('latitiiude', models.DecimalField(decimal_places=9, max_digits=12)),
                ('space', models.FloatField()),
                ('price', models.FloatField()),
                ('number_of_people', models.IntegerField()),
                ('features', models.TextField()),
                ('animal_allowed', models.BooleanField()),
                ('min_age', models.IntegerField()),
                ('max_age', models.IntegerField()),
                ('gender', models.CharField(choices=[('Female', 'Female'), ('Male', 'Male')], max_length=500)),
                ('smoke_allowed', models.BooleanField()),
                ('advertisement_status', models.BooleanField()),
                ('note', models.TextField()),
                ('rooms_number', models.IntegerField()),
                ('bathroom', models.IntegerField()),
                ('has_kitchen', models.BooleanField()),
                ('approved_status', models.CharField(default='pending', max_length=500)),
            ],
        ),
    ]
