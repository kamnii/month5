# Generated by Django 4.1.4 on 2022-12-21 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='grade',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default=5, max_length=10),
        ),
    ]
