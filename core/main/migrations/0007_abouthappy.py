# Generated by Django 4.1.5 on 2023-02-02 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_aboutteam'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutHappy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='abouthappy name')),
                ('about', models.TextField(verbose_name='abouthappy about')),
                ('name1', models.CharField(max_length=30, verbose_name='abouthappy name1')),
            ],
        ),
    ]
