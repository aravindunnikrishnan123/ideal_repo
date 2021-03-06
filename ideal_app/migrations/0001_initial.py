# Generated by Django 3.0.1 on 2020-01-16 07:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
                ('total_questions', models.IntegerField()),
                ('total_marks', models.IntegerField()),
                ('duration', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200)),
                ('option1', models.CharField(max_length=20)),
                ('option2', models.CharField(max_length=20)),
                ('option3', models.CharField(max_length=20)),
                ('option4', models.CharField(max_length=20)),
                ('answer', models.CharField(max_length=20)),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ideal_app.Exam')),
            ],
        ),
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=20, unique=True)),
                ('name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=25)),
                ('password', models.CharField(max_length=15)),
                ('gender', models.CharField(max_length=10)),
                ('user', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='StudentExamStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(default='not', max_length=10)),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ideal_app.Exam')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ideal_app.UserDetails')),
            ],
        ),
        migrations.CreateModel(
            name='StudentExamResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark', models.IntegerField()),
                ('user_ans', models.CharField(max_length=20)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ideal_app.Questions')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ideal_app.UserDetails')),
            ],
        ),
    ]
