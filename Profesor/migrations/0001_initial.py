# Generated by Django 2.2.1 on 2019-06-01 20:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('ap_pat', models.CharField(max_length=100)),
                ('ap_mat', models.CharField(max_length=100)),
                ('phone', models.IntegerField()),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], max_length=1)),
                ('birth_date', models.DateField()),
                ('years_experience', models.IntegerField()),
                ('delete', models.BooleanField(default=False)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('edited', models.DateTimeField(blank=True, default=None, null=True)),
            ],
            options={
                'db_table': 'Profesor',
            },
        ),
    ]