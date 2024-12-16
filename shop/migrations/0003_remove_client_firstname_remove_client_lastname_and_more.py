# Generated by Django 5.1.4 on 2024-12-10 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_remove_client_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='firstname',
        ),
        migrations.RemoveField(
            model_name='client',
            name='lastname',
        ),
        migrations.AlterField(
            model_name='client',
            name='first_name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='client',
            name='last_name',
            field=models.CharField(max_length=100),
        ),
    ]
