# Generated by Django 3.1.4 on 2021-01-03 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_auto_20201230_0020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leads',
            name='email',
            field=models.CharField(max_length=50),
        ),
    ]
