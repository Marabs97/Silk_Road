# Generated by Django 4.1.5 on 2023-01-29 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0009_rename_tempinput_tempinput_temp_input'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tempinput',
            name='id',
        ),
        migrations.AddField(
            model_name='tempinput',
            name='ID',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
