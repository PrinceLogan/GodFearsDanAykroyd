# Generated by Django 2.0.6 on 2018-08-22 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deicide', '0005_deicidelist_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deicidelist',
            name='created_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='deicidelistarchive',
            name='created_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
