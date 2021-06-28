# Generated by Django 3.2.4 on 2021-06-22 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tmpapp', '0003_auto_20210622_1206'),
    ]

    operations = [
        migrations.AddField(
            model_name='testmodel',
            name='age',
            field=models.CharField(blank=True, choices=[('~10', '~10'), ('10~19', '10代'), ('20~29', '20代'), ('30~39', '30代'), ('40~49', '40代'), ('50~59', '50代'), ('60~69', '60代'), ('70~79', '70代'), ('80~89', '80代'), ('90~', '90~')], max_length=10, null=True, verbose_name='age'),
        ),
        migrations.AddField(
            model_name='testmodel',
            name='date',
            field=models.DateField(auto_now=True, null=True, verbose_name='date'),
        ),
        migrations.AddField(
            model_name='testmodel',
            name='files',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='files'),
        ),
        migrations.AddField(
            model_name='testmodel',
            name='number',
            field=models.IntegerField(blank=True, null=True, verbose_name='number'),
        ),
    ]
