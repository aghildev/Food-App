# Generated by Django 3.2 on 2021-08-17 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodapp', '0002_item_item_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='Item_image',
            field=models.CharField(default='https://www.food4fuel.com/wp-content/uploads/woocommerce-placeholder-600x600.png', max_length=500),
        ),
    ]
