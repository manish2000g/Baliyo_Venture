# Generated by Django 4.1.7 on 2023-04-03 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Team', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='department',
            field=models.CharField(help_text='Department of team member', max_length=100),
        ),
    ]
