# Generated by Django 2.0 on 2019-05-14 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20190511_1149'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.TextField()),
                ('event_longitude', models.FloatField()),
                ('event_latitude', models.FloatField()),
                ('event_describe', models.TextField()),
            ],
        ),
    ]
