# Generated by Django 4.2.3 on 2023-07-21 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('country', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='name_official',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
    ]
