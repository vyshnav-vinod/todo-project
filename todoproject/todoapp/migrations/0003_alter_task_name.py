# Generated by Django 5.0.1 on 2024-01-14 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0002_task_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='name',
            field=models.TextField(max_length=100),
        ),
    ]
