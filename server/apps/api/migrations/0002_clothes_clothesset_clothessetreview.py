# Generated by Django 3.0.4 on 2020-03-18 12:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clothes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upper_category', models.CharField(choices=[(1, 'Top'), (2, 'Bottom'), (3, 'Outer'), (4, 'Dress'), (5, 'Skirt')], max_length=30)),
                ('lower_category', models.CharField(choices=[(1, 'Jeans'), (2, 'Knitwear'), (3, 'Jacket')], max_length=30)),
                ('image_url', models.URLField(unique=True)),
                ('alias', models.CharField(max_length=30, null=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ClothesSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('style', models.CharField(max_length=30)),
                ('image_url', models.URLField(unique=True)),
                ('chothes', models.ManyToManyField(to='api.Clothes')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ClothesSetReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_datetime', models.DateTimeField()),
                ('end_datetime', models.DateTimeField()),
                ('location', models.CharField(choices=[(1, '서울특별시'), (2, '천안시'), (3, '부산광역시')], max_length=50)),
                ('review', models.CharField(choices=[(1, 'Warm'), (2, 'Cool'), (3, 'Hot'), (4, 'Cold')], max_length=30)),
                ('max_temp', models.FloatField()),
                ('min_temp', models.FloatField()),
                ('max_sensible_temp', models.FloatField()),
                ('min_sensible_temp', models.FloatField()),
                ('humidity', models.IntegerField()),
                ('wind_speed', models.FloatField()),
                ('precipitation', models.IntegerField()),
                ('clothes_set', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.ClothesSet')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
