# Generated by Django 3.1.1 on 2020-09-28 19:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ExamManagement', '0003_exam_exam_question'),
        ('AnswerManagement', '0003_auto_20200929_0023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examineecustomanswer',
            name='exam',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ExamManagement.attemptedexam'),
        ),
    ]
