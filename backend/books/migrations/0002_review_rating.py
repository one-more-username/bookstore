# Generated by Django 4.2 on 2023-04-28 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='rating',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]