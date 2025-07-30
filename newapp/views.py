from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Question
from django.utils import timezone 


# Create your views here.

def home(request):
    questions = Question.objects.filter(published_date__lte=timezone.now()).order_by("published_date")
    return render(request, "newapp/home.html",{'questions': questions})

def question_detail(request,pk):
    question = get_object_or_404(Question,pk=pk)
    return render(request, "newapp/question_detail.html",{"questions":question})
