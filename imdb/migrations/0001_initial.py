# Generated by Django 3.2.6 on 2021-09-02 12:38

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last', models.CharField(max_length=20)),
                ('first', models.CharField(max_length=20)),
                ('img', models.ImageField(blank=True, null=True, upload_to='directors/')),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('year', models.IntegerField(default=0)),
                ('img', models.ImageField(blank=True, null=True, upload_to='movies/')),
                ('plot', models.FileField(blank=True, null=True, upload_to='plots/')),
                ('rating', models.FloatField(default=5.0)),
                ('views', models.ImageField(default=0, upload_to='')),
                ('director', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='imdb.director')),
            ],
        ),
        migrations.CreateModel(
            name='MovieComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=120)),
                ('author', models.CharField(max_length=32)),
                ('published', models.DateTimeField(default=datetime.datetime.now)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='imdb.movie')),
            ],
        ),
    ]
