# Generated by Django 2.0.1 on 2018-10-20 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coolie', '0004_employee_profilepic'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='contactNo',
            field=models.CharField(default=0, max_length=13),
        ),
    ]
