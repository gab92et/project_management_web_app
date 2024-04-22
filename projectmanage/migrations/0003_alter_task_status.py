# Generated by Django 5.0.4 on 2024-04-22 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectmanage', '0002_task_advancement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('NS', 'Non Started'), ('IP', 'In Progress'), ('CP', 'Completed')], default='NS', max_length=5),
        ),
    ]
