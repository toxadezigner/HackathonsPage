# Generated by Django 3.0.4 on 2020-05-20 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reg', '0026_auto_20200520_1255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventsmodel',
            name='small_description',
            field=models.TextField(help_text='Введите краткое описание', max_length=200),
        ),
    ]
