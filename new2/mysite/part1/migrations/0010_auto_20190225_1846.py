# Generated by Django 2.1.7 on 2019-02-25 16:46

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('part1', '0009_product_favourite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='favourite',
            field=models.ManyToManyField(related_name='favourite', to=settings.AUTH_USER_MODEL),
        ),
    ]