# Generated by Django 3.0.8 on 2020-09-25 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_auto_20200923_1243'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitemmodel',
            name='statu',
            field=models.CharField(default='Active', max_length=50),
        ),
    ]
