# Generated by Django 4.1 on 2023-05-12 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appname', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='heroe',
            name='alignment',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='heroe',
            name='gender',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='heroe',
            name='race',
            field=models.CharField(max_length=40, null=True),
        ),
    ]