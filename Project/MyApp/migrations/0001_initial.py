# Generated by Django 4.1.4 on 2023-01-22 09:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfileModel',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=30)),
                ('middle_name', models.CharField(blank=True, max_length=30, null=True)),
                ('last_name', models.CharField(max_length=30)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=20)),
                ('phone_number', models.CharField(max_length=14, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=16)),
                ('access_level', models.CharField(choices=[('L1', 'Patient'), ('L2', 'Doctor'), ('L3', 'Company')], default='L1', max_length=3)),
                ('tokens', models.PositiveSmallIntegerField(default=2)),
            ],
            options={
                'verbose_name_plural': 'List of Members',
                'ordering': ['last_name'],
            },
        ),
        migrations.CreateModel(
            name='Supervisor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list_patients', models.ManyToManyField(to='MyApp.userprofilemodel')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='MyApp.userprofilemodel')),
            ],
        ),
        migrations.CreateModel(
            name='Results',
            fields=[
                ('report_ID', models.AutoField(primary_key=True, serialize=False)),
                ('result', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyApp.userprofilemodel')),
            ],
        ),
    ]
