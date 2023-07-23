# Generated by Django 4.2.3 on 2023-07-23 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meal_name', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('area', models.CharField(max_length=100)),
                ('instructions', models.TextField()),
                ('meal_image', models.CharField(blank=True, max_length=100)),
                ('tags', models.CharField(blank=True, max_length=100)),
                ('youtube_link', models.CharField(blank=True, max_length=100)),
                ('ingredients_and_measures', models.JSONField()),
            ],
        ),
    ]