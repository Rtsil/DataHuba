# Generated by Django 4.2.3 on 2023-07-24 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0003_rename_category_name_foodcategory_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.CharField(max_length=100)),
            ],
        ),
    ]
