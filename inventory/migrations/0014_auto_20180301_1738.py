# Generated by Django 2.0.1 on 2018-03-01 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0013_auto_20180218_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipped_item',
            name='item_table_name',
            field=models.CharField(choices=[('module', 'module'), ('sensor', 'sensor'), ('pcb', 'pcb'), ('plate', 'plate')], max_length=20),
        ),
    ]
