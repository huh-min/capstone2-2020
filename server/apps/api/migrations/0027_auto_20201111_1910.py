# Generated by Django 3.0.7 on 2020-11-11 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0026_auto_20201111_1844'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clothes',
            name='category_num',
        ),
        migrations.AddField(
            model_name='clothes',
            name='categories',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
