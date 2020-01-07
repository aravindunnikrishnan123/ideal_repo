from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from datetime import datetime
# Create your views here.

def fn_index(request):
    return render(request,'index.html')

def fn_home(request):
    return render(request,'admin_home.html')

def fn_saveUser(request):
    return render(request,'user_reg.html')

def fn_createExam(request):
        if request.method == 'POST':
            title      = request.POST['title']
            total_ques = request.POST['total_ques']
            marks      = request.POST['marks']
            duration   = request.POST['duration']
            try:
                time_duration = '00:'+duration+':00'
                time_duration = datetime.strptime(time_duration,'%H:%M:%S').time()
                exam_obj = Exam(title=title,total_questions=total_ques,total_marks=marks,
                                duration=time_duration)
                exam_obj.save()
                
                if exam_obj.id > 0:
                    request.session['exam_id'] = exam_obj.id
                    return render(request,'questions.html')
            except Exception as e:
                print(e)
                return render(request,'exam.html')
    
        return render(request,'exam.html')

def fn_addQuestion(request):
    exam_id = request.session['exam_id']
    exam    = Exam.objects.get(id=exam_id)
    try:
        question = request.POST['question']
        option1  = request.POST['opt1']
        option2  = request.POST['opt2']
        option3  = request.POST['opt3']
        option4  = request.POST['opt4']
        answer   = request.POST['ans']

        question_obj = Questions(question=question,option1=option1,option2=option2,
                                option3=option3,option4=option4,answer=answer,exam=exam)
        question_obj.save()
        if question_obj.id > 0:
            total_ques = Questions.objects.filter(exam=exam_id).count()
        if total_ques >= exam.total_questions:
            return render(request,'admin_home.html',{'message':'Exam Created Successfully'})

    except Exception as e:
        print(e)
        return HttpResponse('failed')
    return render(request,'questions.html')

