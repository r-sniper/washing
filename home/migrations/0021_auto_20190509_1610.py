# Generated by Django 2.1.1 on 2019-05-09 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_auto_20190509_0403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.IntegerField(default=1, max_length=1),
        ),
    ]
