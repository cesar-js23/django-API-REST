# Generated by Django 3.2.7 on 2021-09-06 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45)),
                ('apellido', models.CharField(max_length=45)),
                ('telefono', models.IntegerField()),
                ('correo', models.EmailField(max_length=254)),
                ('direccion', models.CharField(max_length=100)),
            ],
        ),
    ]
