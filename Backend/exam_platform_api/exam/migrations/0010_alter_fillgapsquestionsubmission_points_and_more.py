# Generated by Django 5.0 on 2024-06-20 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0009_rename_examresults_examresult_alter_exam_password_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fillgapsquestionsubmission',
            name='points',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=4),
        ),
        migrations.AlterField(
            model_name='freetextquestionsubmission',
            name='points',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=4),
        ),
        migrations.AlterField(
            model_name='mcqquestionsubmission',
            name='points',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=4),
        ),
        migrations.AlterField(
            model_name='truefalsequestionsubmission',
            name='points',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=4),
        ),
    ]
