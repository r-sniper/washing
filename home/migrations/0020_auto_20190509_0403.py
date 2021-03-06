# Generated by Django 2.1.1 on 2019-05-08 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_auto_20190509_0304'),
    ]

    operations = [
        migrations.CreateModel(
            name='Money',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(unique=True)),
                ('total_income', models.FloatField(default=0)),
                ('total_expenditure', models.FloatField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='expense',
            name='cost',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='price',
            name='cost',
            field=models.FloatField(),
        ),
    ]
