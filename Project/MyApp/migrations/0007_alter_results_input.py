# Generated by Django 4.1.5 on 2023-01-29 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0006_results_input'),
    ]

    operations = [
        migrations.AlterField(
            model_name='results',
            name='input',
            field=models.TextField(default='Default'),
        ),
    ]