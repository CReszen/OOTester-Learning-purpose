from django.urls import path
from . import views

app_name = "task"
urlpatterns=[
    path('',views.showMenu,name='menu'),
    path('<int:question_id>/',views.showQuestion,name='quest'),
    path('<int:id>',views.changeValue,name='change'),
    path('reset/',views.resetQuestion,name='reset'),
    path('user/',views.getUser,name='user'),
]
