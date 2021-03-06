# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-23 21:26
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('amount', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='BetTeam',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('bet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Bet')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('TeamId', models.AutoField(primary_key=True, serialize=False)),
                ('team_name', models.CharField(max_length=30, null=True, unique=True)),
                ('rating', models.PositiveSmallIntegerField(null=True, unique=True)),
                ('sport', models.CharField(max_length=30, null=True)),
                ('number_of_players', models.PositiveSmallIntegerField(null=True)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='pics/')),
            ],
        ),
        migrations.CreateModel(
            name='User1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20, null=True)),
                ('last_name', models.CharField(max_length=20, null=True)),
                ('phone', models.PositiveIntegerField(null=True, unique=True)),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('passport', models.PositiveIntegerField(null=True, unique=True)),
                ('user1', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='betteam',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Team'),
        ),
        migrations.AddField(
            model_name='bet',
            name='team',
            field=models.ManyToManyField(through='app.BetTeam', to='app.Team'),
        ),
        migrations.AddField(
            model_name='bet',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.User1'),
        ),
    ]
