# Generated by Django 3.2.4 on 2021-06-28 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0016_myscenariomodel_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArtModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100)),
                ('summary', models.CharField(blank=True, max_length=300)),
                ('script', models.CharField(blank=True, max_length=10000)),
            ],
        ),
    ]
