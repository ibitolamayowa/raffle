# Generated by Django 3.1.7 on 2021-03-07 23:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0002_transaction_payment_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='payment_link',
        ),
    ]
