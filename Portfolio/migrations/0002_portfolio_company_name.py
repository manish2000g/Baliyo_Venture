# Generated by Django 4.1.3 on 2023-03-22 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='company_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
