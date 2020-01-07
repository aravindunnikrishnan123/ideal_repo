from django.urls import path
from . import views

urlpatterns = [
    path('',views.fn_index),
    path('home/',views.fn_home),
    path('saveuser/',views.fn_saveUser),
    path('create-exam/',views.fn_createExam),
    path('add-questions/',views.fn_addQuestion)
]