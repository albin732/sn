# Generated by Django 3.0.7 on 2020-09-18 03:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0003_orderstack_orders_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderstack',
            old_name='orders_id',
            new_name='order_fk',
        ),
    ]
