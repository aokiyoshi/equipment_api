# Generated by Django 4.0.6 on 2022-07-09 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_equipment_equipment_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='EquipmentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16)),
                ('description', models.CharField(max_length=144)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]