# Generated by Django 3.0.1 on 2020-01-03 12:08

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
                ('title', models.CharField(max_length=50)),
                ('total_questions', models.IntegerField()),
                ('total_marks', models.IntegerField()),
                ('duration', models.TimeField()),
            ],
        ),
    ]
