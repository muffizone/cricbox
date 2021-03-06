# Generated by Django 3.1.5 on 2021-01-23 22:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('match_statistics', '__first__'),
        ('player', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bowler',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('overs', models.PositiveIntegerField(default=0, verbose_name='Overs')),
                ('maidens', models.PositiveIntegerField(blank=True, default=0, verbose_name='Maidens')),
                ('runs', models.PositiveIntegerField(default=0, verbose_name='Runs')),
                ('wickets', models.PositiveIntegerField(default=0, verbose_name='Wickets')),
                ('match_statistics', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='match_statistics.matchstatistics')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='player.player')),
            ],
            options={
                'db_table': 'bowlers',
                'ordering': ['player'],
            },
        ),
    ]
