# Generated by Django 3.2.6 on 2021-09-16 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imdb', '0002_auto_20210915_1705'),
    ]

    operations = [
        migrations.AddField(
            model_name='director',
            name='bio',
            field=models.FileField(blank=True, null=True, upload_to='bio/'),
        ),
    ]
