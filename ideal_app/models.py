from django.db import models

# Create your models here.

class UserDetails(models.Model):
    user_id  = models.CharField(max_length=20, unique=True)
    name     = models.CharField(max_length=30)
    email    = models.CharField(max_length=25)
    password = models.CharField(max_length=15)
    gender   = models.CharField(max_length=10)
    user     = models.CharField(max_length=10)
   

class Exam(models.Model):
    title           = models.CharField(max_length=50)
    description     = models.CharField(max_length=100)
    total_questions = models.IntegerField()
    total_marks     = models.IntegerField()
    duration        = models.IntegerField()

class Questions(models.Model):
    question  = models.CharField(max_length=200)
    option1   = models.CharField(max_length=20)
    option2   = models.CharField(max_length=20)
    option3   = models.CharField(max_length=20)
    option4   = models.CharField(max_length=20)
    answer    = models.CharField(max_length=20)
    exam      = models.ForeignKey(Exam, on_delete=models.CASCADE)

        
class StudentExamResult(models.Model):
    student     = models.ForeignKey(UserDetails,on_delete=models.CASCADE)
    question    = models.ForeignKey(Questions,on_delete=models.CASCADE)
    mark        = models.IntegerField()
    user_ans    = models.CharField(max_length=20)
    time_taken  = models.IntegerField()

class StudentExamStatus(models.Model):
    student   = models.ForeignKey(UserDetails,on_delete=models.CASCADE)
    exam      = models.ForeignKey(Exam, on_delete=models.CASCADE)
    status    = models.CharField(max_length=10)
