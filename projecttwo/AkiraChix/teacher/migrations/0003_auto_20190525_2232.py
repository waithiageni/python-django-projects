# Generated by Django 2.2.1 on 2019-05-25 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0002_auto_20190525_2157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='number_of_units',
            field=models.CharField(max_length=5),
        ),
    ]
