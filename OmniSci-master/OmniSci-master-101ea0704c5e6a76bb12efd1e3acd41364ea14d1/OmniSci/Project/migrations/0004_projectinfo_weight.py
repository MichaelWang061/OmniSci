# Generated by Django 2.1.7 on 2019-07-16 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0003_projectinfo_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectinfo',
            name='weight',
            field=models.IntegerField(default=-100, verbose_name='排序权重'),
        ),
    ]
