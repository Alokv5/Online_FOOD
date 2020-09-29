# Generated by Django 3.0.8 on 2020-09-23 07:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0001_initial'),
        ('customer', '0002_cartitemmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitemmodel',
            name='quantity',
            field=models.IntegerField(default=False),
        ),
        migrations.AlterField(
            model_name='cartitemmodel',
            name='customer',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='customer.CustomerRegistrationModel'),
        ),
        migrations.AlterField(
            model_name='cartitemmodel',
            name='food',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='vendor.FoodItemsModel'),
        ),
    ]