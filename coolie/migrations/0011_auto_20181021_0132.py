# Generated by Django 2.0.1 on 2018-10-21 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coolie', '0010_auto_20181021_0119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='userid',
            field=models.CharField(max_length=300),
        ),
    ]
