# Generated by Django 4.1.4 on 2022-12-21 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0003_alter_review_grade_alter_review_movie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='grade',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=1),
        ),
    ]