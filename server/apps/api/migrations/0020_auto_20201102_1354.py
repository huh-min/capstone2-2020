# Generated by Django 3.0.7 on 2020-11-02 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_clothessetreview_weather_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('M', 'M'), ('W', 'W')], max_length=2),
        ),
    ]
