# Generated by Django 3.0.3 on 2020-09-18 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campgrounds', '0007_log'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campground',
            name='camp_id',
            field=models.CharField(max_length=10),
        ),
    ]
