# Generated by Django 2.2.1 on 2019-05-23 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Administrador', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='administrador',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]
