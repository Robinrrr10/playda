# Generated by Django 2.2.6 on 2019-10-09 17:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20191009_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='postedOn',
            field=models.DateTimeField(blank=True, null=True, verbose_name=django.utils.timezone.now),
        ),
    ]