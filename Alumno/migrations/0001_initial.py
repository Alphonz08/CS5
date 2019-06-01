# Generated by Django 2.2.1 on 2019-06-01 20:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Profesor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('ap_pat', models.CharField(max_length=100)),
                ('ap_mat', models.CharField(max_length=100)),
                ('id_number', models.IntegerField()),
                ('address', models.CharField(max_length=100)),
                ('subject', models.CharField(choices=[('PCS', 'Programacion cliente servidor'), ('SID', 'Sistemas digitales'), ('ARS', 'Arquitectura de software'), ('FUR', 'Fundamentos de redes')], default='PCS', max_length=3)),
                ('phone', models.IntegerField()),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], max_length=1)),
                ('birthdate', models.DateField()),
                ('delete', models.BooleanField(default=False)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('edited', models.DateTimeField(blank=True, default=None, null=True)),
                ('teacher', models.ForeignKey(on_delete=models.SET(-1), to='Profesor.Profesor')),
            ],
            options={
                'db_table': 'Alumno',
            },
        ),
    ]
