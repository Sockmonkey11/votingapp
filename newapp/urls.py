from django.urls import path
from . import views

urlpatterns = [
    path("",views.home, name = "home"),
    path("question/<int:pk>/",views.question_detail, name = "question_detail"),
    path("question/new/", views.question_new, name = "question_new"),
    path("question/<int:pk>/edit/", views.question_edit,name = "question_edit")
]