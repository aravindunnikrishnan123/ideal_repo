from django.urls import path
from . import views

urlpatterns = [
    path('',views.fn_index),
    path('login/',views.fn_userLogin),
    path('saveuser/',views.fn_saveUser),
    path('create-exam/',views.fn_createExam),
    path('add-questions/',views.fn_addQuestion),
    path('viewexams/',views.fn_viewExams),
    path('select-exam/',views.fn_selectExam),
    path('getquestions/',views.fn_getQuestions),
    path('logout/',views.fn_logOut)
]