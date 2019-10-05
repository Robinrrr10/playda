# Generated by Django 2.2.6 on 2019-10-04 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postType', models.CharField(max_length=50)),
                ('postedBy', models.IntegerField()),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='postedImages')),
                ('isActive', models.BooleanField(default=True)),
            ],
        ),
    ]