# Generated by Django 3.1.7 on 2021-05-04 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_auto_20210504_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='identifier',
            field=models.CharField(default='20P36', max_length=5),
        ),
    ]
