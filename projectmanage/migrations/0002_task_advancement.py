# Generated by Django 5.0.4 on 2024-04-22 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectmanage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='advancement',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]