# Generated by Django 3.0.8 on 2020-09-25 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_cartitemmodel_statu'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordermodel',
            name='items',
        ),
        migrations.RemoveField(
            model_name='ordermodel',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='ordermodel',
            name='status',
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='c_id',
            field=models.ManyToManyField(to='customer.CartItemModel'),
        ),
    ]
