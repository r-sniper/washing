# Generated by Django 2.1.1 on 2019-05-08 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_auto_20190508_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]