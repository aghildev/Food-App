# Generated by Django 3.2 on 2021-08-16 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='Item_image',
            field=models.CharField(default='https://s3.amazonaws.com/ODNUploads/56394e2bb0221placeholder_food_item_2.png', max_length=500),
        ),
    ]
