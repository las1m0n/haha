# Generated by Django 2.1.7 on 2019-02-21 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('part1', '0007_auto_20190217_2233'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='items',
        ),
        migrations.AddField(
            model_name='order',
            name='items',
            field=models.ForeignKey(default=1, on_delete=True, to='part1.Cart'),
            preserve_default=False,
        ),
    ]
