# Generated by Django 5.0 on 2024-06-23 11:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('group', '__first__'),
        ('instructor', '__first__'),
        ('student', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=250, null=True)),
                ('duration_minutes', models.IntegerField(default=60)),
                ('starting_date', models.DateTimeField(null=True)),
                ('finishing_date', models.DateTimeField(blank=True, null=True)),
                ('started', models.BooleanField(default=False)),
                ('finished', models.BooleanField(default=False)),
                ('max_marks', models.IntegerField(default=100)),
                ('password', models.CharField(blank=True, max_length=1024, null=True)),
                ('review', models.BooleanField(default=False)),
                ('group', models.ManyToManyField(to='group.group')),
                ('instructor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='instructor.instructor')),
                ('student', models.ManyToManyField(to='student.student')),
            ],
        ),
        migrations.CreateModel(
            name='ExamStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attempted', models.BooleanField(default=False)),
                ('finished', models.BooleanField(default=False)),
                ('attempted_at', models.DateTimeField(null=True)),
                ('finished_at', models.DateTimeField(null=True)),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.exam')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.student')),
            ],
        ),
        migrations.CreateModel(
            name='ExamSubmission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('new_tab', models.IntegerField(default=0)),
                ('exam_status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.examstatus')),
            ],
        ),
        migrations.CreateModel(
            name='CheatingCase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_spent_cheating', models.FloatField(default=0.0)),
                ('time_no_person_present', models.FloatField(default=0.0)),
                ('image', models.ImageField(upload_to='')),
                ('submission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cheating_cases', to='exam.examsubmission')),
            ],
        ),
        migrations.CreateModel(
            name='FillGapsQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200)),
                ('points', models.DecimalField(decimal_places=2, max_digits=4)),
                ('correct_answers', models.JSONField()),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.exam')),
            ],
        ),
        migrations.CreateModel(
            name='FillGapsQuestionSubmission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.JSONField()),
                ('points', models.DecimalField(decimal_places=2, default=0.0, max_digits=4)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.fillgapsquestion')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.student')),
            ],
        ),
        migrations.CreateModel(
            name='FreeTextQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200)),
                ('points', models.DecimalField(decimal_places=2, max_digits=4)),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.exam')),
            ],
        ),
        migrations.CreateModel(
            name='FreeTextQuestionSubmission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.JSONField()),
                ('points', models.DecimalField(decimal_places=2, default=0.0, max_digits=4)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.freetextquestion')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.student')),
            ],
        ),
        migrations.CreateModel(
            name='MCQQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200)),
                ('points', models.DecimalField(decimal_places=2, max_digits=4)),
                ('answer_options', models.JSONField()),
                ('correct_answers', models.JSONField()),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.exam')),
            ],
        ),
        migrations.CreateModel(
            name='MCQQuestionSubmission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.JSONField()),
                ('points', models.DecimalField(decimal_places=2, default=0.0, max_digits=4)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.mcqquestion')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.student')),
            ],
        ),
        migrations.CreateModel(
            name='TrueFalseQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200)),
                ('points', models.DecimalField(decimal_places=2, max_digits=4)),
                ('correct_answer', models.BooleanField()),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.exam')),
            ],
        ),
        migrations.CreateModel(
            name='TrueFalseQuestionSubmission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.BooleanField()),
                ('points', models.DecimalField(decimal_places=2, default=0.0, max_digits=4)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.truefalsequestion')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.student')),
            ],
        ),
    ]
