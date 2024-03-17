# Generated by Django 4.0.5 on 2023-03-20 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SampleData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guid', models.CharField(max_length=100)),
                ('geo_latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('geo_longitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('date_y_m_d', models.DateField()),
                ('numeric_00', models.FloatField()),
                ('numeric_01', models.FloatField()),
            ],
        ),
    ]
