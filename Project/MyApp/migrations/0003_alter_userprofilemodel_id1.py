# Generated by Django 4.1.5 on 2023-01-27 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0002_alter_userprofilemodel_id1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofilemodel',
            name='ID1',
            field=models.PositiveSmallIntegerField(auto_created=True, unique=True),
        ),
    ]
