from django.db import models

# Create your models here.
class Exam(models.Model):
    title           = models.CharField(max_length=50)
    total_questions = models.IntegerField()
    total_marks     = models.IntegerField()
    duration        = models.TimeField()

class Questions(models.Model):
    question  = models.CharField(max_length=200)
    option1   = models.CharField(max_length=20)
    option2   = models.CharField(max_length=20)
    option3   = models.CharField(max_length=20)
    option4   = models.CharField(max_length=20)
    answer    = models.CharField(max_length=20)
    exam      = models.ForeignKey(Exam, on_delete=models.CASCADE)
