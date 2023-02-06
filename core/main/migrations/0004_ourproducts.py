# Generated by Django 4.1.5 on 2023-01-31 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_homeabout_alter_homeproducts_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='OurProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='ourproduct name')),
                ('about', models.TextField(verbose_name='ourproduct about')),
                ('img', models.ImageField(upload_to='media', verbose_name='ourproduct image')),
                ('price', models.IntegerField(verbose_name='ourproduct price')),
            ],
        ),
    ]
