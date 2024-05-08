# Generated by Django 5.0 on 2024-05-08 01:45

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('instructor', '0001_initial'),
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, max_length=200)),
                ('code', models.UUIDField(editable=False, unique=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('instructor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instructor.instructor')),
                ('students', models.ManyToManyField(to='student.student')),
            ],
        ),
    ]
