# Generated by Django 5.0.4 on 2024-05-15 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommender', '0003_orders_orderupdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='Y_Pub',
            field=models.IntegerField(default=1950),
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.CharField(default='Not available', max_length=500),
        ),
        migrations.AddField(
            model_name='book',
            name='rating',
            field=models.FloatField(default=0.0),
        ),
    ]