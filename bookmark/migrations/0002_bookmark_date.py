# Generated by Django 3.1.7 on 2021-03-25 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmark', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmark',
            name='date',
            field=models.DateTimeField(null=True, verbose_name='DATETIME'),
        ),
    ]