# Generated by Django 3.1.7 on 2021-05-27 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0006_auto_20210521_0943'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='slug',
            field=models.SlugField(default=1, max_length=255, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='listing',
            name='identifier',
            field=models.CharField(default='D5WPM', max_length=5),
        ),
    ]