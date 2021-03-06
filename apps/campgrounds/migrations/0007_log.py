# Generated by Django 3.0.3 on 2020-09-14 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campgrounds', '0006_auto_20200914_0503'),
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True)),
                ('count', models.IntegerField(null=True)),
                ('start_id', models.IntegerField(default=None)),
                ('end_id', models.IntegerField(default=None)),
            ],
            options={
                'ordering': ['date'],
            },
        ),
    ]
