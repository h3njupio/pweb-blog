# Generated by Django 2.0.2 on 2018-02-22 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parsed_data', '0006_auto_20180223_0849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogdata',
            name='link',
            field=models.CharField(max_length=500),
        ),
    ]
