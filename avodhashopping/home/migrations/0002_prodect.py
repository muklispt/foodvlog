# Generated by Django 5.0.6 on 2024-05-15 09:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='prodect',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('img', models.ImageField(upload_to='prodect')),
                ('dic', models.TextField()),
                ('stock', models.IntegerField()),
                ('avilable', models.BooleanField()),
                ('price', models.IntegerField()),
                ('categpry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.categ')),
            ],
        ),
    ]
