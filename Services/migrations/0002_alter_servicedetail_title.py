# Generated by Django 4.1.3 on 2023-03-23 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicedetail',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]