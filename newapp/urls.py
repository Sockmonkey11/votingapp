from django.urls import path
from . import views

urlpatterns = [
    path("",views.home, name = "home"),
    path("post/<int:pk>/",views.question_detail, name = "question_detail")
]