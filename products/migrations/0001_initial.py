# Generated by Django 5.0.3 on 2024-04-02 06:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fertilisers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pebbles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Plants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pots',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Seeds',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Fertilisers_Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=100, null=True)),
                ('description', models.TextField(max_length=400, null=True)),
                ('image', models.ImageField(null=True, upload_to='Fertilisers')),
                ('price', models.FloatField(null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.fertilisers')),
            ],
        ),
        migrations.CreateModel(
            name='Pebbles_Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=100, null=True)),
                ('description', models.TextField(max_length=400, null=True)),
                ('image', models.ImageField(null=True, upload_to='Pebbles')),
                ('price', models.FloatField(null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.pebbles')),
            ],
        ),
        migrations.CreateModel(
            name='Plants_Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=100, null=True)),
                ('description', models.TextField(max_length=400, null=True)),
                ('image', models.ImageField(null=True, upload_to='plants')),
                ('price', models.FloatField(null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.plants')),
            ],
        ),
        migrations.CreateModel(
            name='Pots_Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=100, null=True)),
                ('description', models.TextField(max_length=400, null=True)),
                ('image', models.ImageField(null=True, upload_to='Pots')),
                ('price', models.FloatField(null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.pots')),
            ],
        ),
        migrations.CreateModel(
            name='Seeds_Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=100, null=True)),
                ('description', models.TextField(max_length=400, null=True)),
                ('image', models.ImageField(null=True, upload_to='Seeds')),
                ('price', models.FloatField(null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.seeds')),
            ],
        ),
    ]