# Generated by Django 2.0.2 on 2018-02-22 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parsed_data', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogdata',
            name='link',
            field=models.URLField(default=11),
            preserve_default=False,
        ),
    ]