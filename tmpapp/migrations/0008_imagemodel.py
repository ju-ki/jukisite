# Generated by Django 3.2.4 on 2021-06-25 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tmpapp', '0007_auto_20210624_2025'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('background_image', models.ImageField(upload_to='img/upload')),
                ('description', models.TextField(default='This is my favorite photo', max_length=200)),
            ],
        ),
    ]
