# Generated by Django 4.1.3 on 2023-03-20 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ResearchAndDevelopment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='static/images')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(max_length=500)),
            ],
        ),
    ]
