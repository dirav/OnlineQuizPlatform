# Generated by Django 3.1.1 on 2020-09-17 14:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ExamManagement', '0006_custom_questions'),
        ('AnswerManagement', '0003_auto_20200916_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ExamManagement.mcq_questions'),
        ),
    ]