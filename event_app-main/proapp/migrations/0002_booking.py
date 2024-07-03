# Generated by Django 5.0.2 on 2024-06-10 08:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cus_name', models.CharField(max_length=55)),
                ('cus_ph', models.CharField(max_length=12)),
                ('booinkg_date', models.DateField()),
                ('booinkg_on', models.DateField(auto_now=True)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proapp.event')),
            ],
        ),
    ]
