# Generated by Django 4.2 on 2025-01-14 22:46

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('sku', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField()),
                ('shop', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
                ('discount', models.IntegerField(default=0)),
                ('category', models.CharField(max_length=255)),
                ('stock', models.IntegerField()),
                ('is_available', models.BooleanField(default=True)),
                ('picture', models.URLField(max_length=2048)),
            ],
        ),
    ]
