# Generated by Django 3.1.5 on 2021-01-12 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DateOfExamCreation', models.DateField()),
                ('ExamName', models.TextField(default='')),
                ('Subject', models.CharField(max_length=50)),
                ('Batch', models.IntegerField(default=0)),
                ('Semester', models.IntegerField(default=0)),
                ('Shift', models.IntegerField(default=0)),
                ('Batch_Shift_Exam', models.TextField(default='')),
                ('TotalQuestions', models.IntegerField(default=0)),
                ('TotalTime', models.IntegerField(default=0)),
                ('Started', models.BooleanField(default=False)),
                ('Completed', models.BooleanField(default=False)),
                ('DateOfExamConducted', models.DateTimeField(default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Question', models.TextField()),
                ('Question_Type', models.CharField(default='', max_length=10)),
                ('Option_1', models.TextField()),
                ('Option_2', models.TextField()),
                ('Option_3', models.TextField()),
                ('Option_4', models.TextField()),
                ('Answer', models.TextField()),
                ('Subject', models.CharField(default='', max_length=50)),
                ('ExamName', models.TextField(default='')),
                ('Batch', models.IntegerField(default=0)),
                ('Semester', models.IntegerField(default=0)),
                ('Shift', models.IntegerField(default=0)),
                ('Batch_Shift_Exam', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Pin', models.TextField()),
                ('Marks', models.IntegerField(default=0)),
                ('Subject', models.CharField(max_length=50)),
                ('Shift', models.IntegerField(null=True)),
                ('Semester', models.IntegerField(null=True)),
                ('Batch_Shift_Exam', models.TextField(null=True)),
                ('Time_Taken', models.FloatField(default=float("inf"))),
            ],
        ),
    ]
