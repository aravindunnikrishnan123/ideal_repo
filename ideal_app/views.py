from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse
from datetime import datetime
from django.db.models import Q
# Create your views here.

def fn_index(request):
    return render(request,'index.html')

def fn_userLogin(request):
    if request.method == 'POST':
        email    = request.POST['uname']
        password = request.POST['password']
        try:
            user_obj = UserDetails.objects.get(email=email)
            if user_obj.password == password:
                request.session['user_id'] = user_obj.id
                request.session['user'] = user_obj.user
                return render(request,'home.html')
            return render(request,'index.html',{'pass_msg':'Invalid Password'})
        except Exception as e:
            print(e)
            return render(request,'index.html',{'uname_msg':'Invalid UserName'})
    if 'user' in request.session:
        return render(request,'home.html')
    return redirect('/')

def fn_saveUser(request):
    if request.method == 'POST':
        email = request.POST['email']
        user_exist = UserDetails.objects.filter(email=email).exists()
        if not user_exist:
            user_id  = request.POST['user_id']
            name     = request.POST['name']
            password = request.POST['password']
            gender   = request.POST['gender']
            user     = request.POST['user']

            try:
                user_obj = UserDetails(user_id=user_id,name=name,email=email,
                                    password=password,gender=gender,user=user)
                user_obj.save()
                return render(request,'home.html',{'message':'User Registration done successfully'})
            except:
                return render(request,'home.html',{'message':'some thing went wrong Try Again !!!'})
    else:
        user = request.GET['type']
        return render(request,'user_reg.html',{'user':user})

def fn_createExam(request):
        if request.method == 'POST':
            title           = request.POST['title']
            description     = request.POST['description']
            total_ques      = request.POST['total_ques']
            marks           = request.POST['marks']
            time_duration   = request.POST['duration']
            try:
                exam_obj = Exam(title=title,description=description,
                            total_questions=total_ques,total_marks=marks,
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
    if request.method == 'GET':
        return redirect('/login')

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
            return render(request,'home.html',{'message':'Exam Created Successfully'})

    except Exception as e:
        print(e)
        return HttpResponse('failed')
    return render(request,'questions.html')

def fn_viewExams(request):
    student_id = request.session['user_id']
    exam_list  = []
    exam_obj   = '' 
    student_exist = StudentExamStatus.objects.filter(student=student_id).exists()
    
    if student_exist:
        # the student_exam_status queryset returns exam id which students have finished.
        attended_exam = []
        attended_exams_obj = StudentExamStatus.objects.filter(student=student_id)
        for e in attended_exams_obj:
            attended_exam.append(e.exam.id)  
        # The queryset return exams which were not finished by the student.
            exam_obj = Exam.objects.filter().exclude(id__in=attended_exam).only('id','title','description')
            if not exam_obj:
                return render(request,'home.html',{'message':"You have taken all the Exam"})
    else:
        exam_obj = Exam.objects.only('id','title','description')
    for e in exam_obj:
        exam_list.append(e)
    return render(request,'exam_menu.html',{'exam_list':exam_list})

def fn_selectExam(request):
    selected_exam_id = request.GET['exam-id']
    exam_obj = Exam.objects.get(id=selected_exam_id)
    request.session['exam_id'] = selected_exam_id    
    return render(request,'exam_template.html',{'exam':exam_obj})

def fn_setExamStatus(request):
    status   = request.GET['status']
    exam_id  = request.session['exam_id']
    exam_obj = Exam.objects.get(id=exam_id)
    student  = UserDetails.objects.get(id=request.session['user_id'])
    try:
        stud_exam_status = StudentExamStatus.objects.get(student=student,exam=exam_obj)
        if stud_exam_status.status == status:
            return redirect('/getquestions')
        stud_exam_status.status = status
        stud_exam_status.save()
        del request.session['exam_id']
        return redirect('/login')
    except:
        stud_exam_status = StudentExamStatus(student=student,exam=exam_obj,status=status)
        stud_exam_status.save()
    return redirect('/getquestions')


def fn_getQuestions(request):
    exam_id = request.session['exam_id']
    exam_obj = Exam.objects.get(id=exam_id)
    student  = UserDetails.objects.get(id=request.session['user_id'])    
    if request.method == 'GET':
        question_obj = Questions.objects.filter(exam=exam_id).first() 
        request.session['question_time'] = exam_obj.duration // exam_obj.total_questions # time taken to complete one question
       
    else:
        cur_ques_id = request.POST['question-id']
        evaluateStudentExam(request.POST,exam_obj,student,request.session['question_time'])
        question_obj = Questions.objects.filter(exam=exam_id,id__gt=cur_ques_id).first()
        if not question_obj:
            return render(request,'exam_template.html',{'response':'finished'})
    return render(request,'exam_template.html',{'question':question_obj,'exam':exam_obj})

#service to evaluate student answer.
def evaluateStudentExam(req_dict,exam_obj,student,time_per_question):
    print(req_dict)
    time_taken = int(req_dict['current-time'])
    user_ans   = 'not explained'
    mark = 0
    question = Questions.objects.get(id=req_dict['question-id'])
    if 'user_ans' in req_dict:
        user_ans = req_dict['user_ans']
        if question.answer == user_ans:
            mark = exam_obj.total_marks / exam_obj.total_questions
    # the below query check if the current question is already answered by the  student.
    question_submitted_obj = StudentExamResult.objects.filter(Q(question=req_dict['question-id']) 
                            &Q(student=student))
    if question_submitted_obj:
        if question_submitted_obj[0].time_taken == int(time_per_question) * 60:# convert into seconds
            #question_obj = Questions.objects.filter(exam=exam_obj,id__gt=req_dict['question-id']).first()
            # this question is already timeout for this student.
            return 0
        else:
            print(time_per_question)
            if question_submitted_obj[0].time_taken + time_taken <= int(time_per_question)*60:
                question_submitted_obj[0].mark = mark
                question_submitted_obj[0].user_ans = user_ans
                question_submitted_obj[0].time_taken += time_taken
                question_submitted_obj[0].save()
    else:
        result_obj = StudentExamResult(student=student,question=question,
                            mark=mark,user_ans=user_ans,time_taken=time_taken)
        result_obj.save()
    return 1
        
def fn_examReport(request):
    if request.method == 'POST':
        student_id = request.POST['student-id']
        exam       = request.POST['exam-id']
        try:
            user = UserDetails.objects.get(user_id=student_id)
            exam_status_obj = StudentExamStatus.objects.get(exam=exam)
            if exam_status_obj.status == 'Finished':
                question_list = []
                questions = Questions.objects.filter(exam=exam)
                total = 0
                for qobj in questions:
                    total += 1
                    question_list.append(qobj.id)

                exam_result_obj = StudentExamResult.objects.filter(student=user,question__in=question_list)
                exam_result_obj.time = questions[0].exam.duration // total * 60
                exam_result_obj.title= questions[0].exam.title
                result_dict = {'result':exam_result_obj}
        except Exception as e:
            print(e)
            return redirect('/exam-report?message=no user')

        return render(request,'report.html',result_dict)
    print(request.GET)
    exams = Exam.objects.only('id','title')
    if 'message' in request.GET:
        return render(request,'report.html',{'exams':exams,'response':'Invalid User ID'})
   
    return render(request,'report.html',{'exams':exams})

def fn_logOut(request):
    del request.session['user']
    return redirect('/')
