# Generated by Django 5.0 on 2023-12-07 19:31

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
                ('nombres', models.CharField(max_length=30)),
                ('apellidos', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=50)),
                ('movil', models.CharField(max_length=13)),
                ('github', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 't_alumnos',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=60)),
                ('comentario', models.CharField(max_length=255)),
                ('fecha', models.DateField(auto_now=True)),
            ],
            options={
                'db_table': 't_comments',
            },
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institucion', models.CharField(default='Codo a Codo', max_length=30)),
                ('curso', models.CharField(default='Full-Stack Python 2023', max_length=30)),
                ('grupo', models.PositiveSmallIntegerField(default=19)),
                ('comision', models.PositiveSmallIntegerField(default=23507)),
            ],
            options={
                'db_table': 't_cursos',
            },
        ),
        migrations.CreateModel(
            name='IaFunction',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('image', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 't_ia_function',
            },
        ),
        migrations.CreateModel(
            name='Ia',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('image', models.CharField(max_length=60)),
                ('link', models.CharField(max_length=255)),
                ('functionList', models.ManyToManyField(to='ias_app.iafunction')),
            ],
            options={
                'db_table': 't_ias',
            },
        ),
    ]
