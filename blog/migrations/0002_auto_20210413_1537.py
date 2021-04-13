# Generated by Django 3.2 on 2021-04-13 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.CharField(blank=True, help_text='simple description text.', max_length=100, verbose_name='DESCRIPTION'),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(allow_unicode=True, help_text='one word for title alias.', unique=True, verbose_name='SLUG'),
        ),
    ]
