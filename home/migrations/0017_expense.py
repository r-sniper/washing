# Generated by Django 2.1.1 on 2019-05-08 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_remove_order_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=60)),
                ('date', models.DateField()),
            ],
        ),
    ]