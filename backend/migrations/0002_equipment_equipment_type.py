# Generated by Django 4.0.6 on 2022-07-09 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipment',
            name='equipment_type',
            field=models.CharField(default=None, max_length=16),
            preserve_default=False,
        ),
    ]
