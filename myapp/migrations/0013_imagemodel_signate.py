# Generated by Django 3.2.4 on 2021-06-26 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_auto_20210626_1409'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagemodel',
            name='signate',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
