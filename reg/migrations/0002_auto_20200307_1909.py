# Generated by Django 3.0.3 on 2020-03-07 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reg', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hack',
            name='visits',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='meetup',
            name='visits',
            field=models.IntegerField(default=0),
        ),
    ]
