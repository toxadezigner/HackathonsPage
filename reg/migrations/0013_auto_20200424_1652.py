# Generated by Django 3.0.4 on 2020-04-24 13:52

import datetime
from django.db import migrations, models
import djrichtextfield.models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('reg', '0012_auto_20200406_2242'),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Введите название хакатона', max_length=200)),
                ('small_description', models.CharField(help_text='Введите краткое описание хакатона', max_length=200)),
                ('hackText', djrichtextfield.models.RichTextField(help_text='Введите полностью условия хакатона')),
                ('pub_date', models.DateField(blank=True, default=datetime.datetime.now)),
                ('image', models.ImageField(default=' ', upload_to='')),
                ('filter', models.CharField(choices=[('online', 'онлайн'), ('offline', 'оффлайн')], default='online', max_length=20)),
                ('filter2', models.CharField(choices=[('hackathon', 'хакатон'), ('meet', 'митап'), ('breakfast', 'завтрак'), ('conference', 'конференция'), ('course', 'курсы')], default='hackathon', max_length=20)),
                ('visits', models.IntegerField(default=0)),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
        ),
        migrations.RemoveField(
            model_name='meetup',
            name='tags',
        ),
        migrations.DeleteModel(
            name='Hack',
        ),
        migrations.DeleteModel(
            name='Meetup',
        ),
    ]