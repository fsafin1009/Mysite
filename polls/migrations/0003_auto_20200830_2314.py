# Generated by Django 3.0.5 on 2020-08-30 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20200830_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.TextField(verbose_name='Описание статьи'),
        ),
    ]
