# Generated by Django 2.1.1 on 2019-05-05 22:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_merge_20190505_2054'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='to_show',
        ),
    ]
