# Generated by Django 2.0.2 on 2018-03-03 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0017_auto_20180303_2059'),
    ]

    operations = [
        migrations.AddField(
            model_name='module',
            name='identifier',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True),
        ),
    ]
