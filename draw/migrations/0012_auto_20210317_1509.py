# Generated by Django 3.1.7 on 2021-03-17 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('draw', '0011_rafflecampaign_winner_announced'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rafflecampaign',
            old_name='winner_announced',
            new_name='campaign_closed',
        ),
        migrations.AlterField(
            model_name='rafflecampaign',
            name='winning_ticket',
            field=models.CharField(blank=True, max_length=6),
        ),
    ]
