from django.shortcuts import render, HttpResponse
from .models import Question
from django.utils import timezone 


# Create your views here.

def home(request):
    questions = Question.objects.filter(published_date__lte=timezone.now()).order_by("published_date")
    return render(request, "newapp/home.html",{'questions': questions})
