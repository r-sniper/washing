# Generated by Django 2.1.1 on 2019-05-08 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_auto_20190509_0117'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='cost',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='expense',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
