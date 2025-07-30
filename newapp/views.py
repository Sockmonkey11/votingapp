from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .models import Question
from django.utils import timezone
from .forms import QuestionForm


# Create your views here.

def home(request):
    questions = Question.objects.filter(published_date__lte=timezone.now()).order_by("published_date")
    return render(request, "newapp/home.html",{'questions': questions})

def question_detail(request,pk):
    question = get_object_or_404(Question,pk=pk)
    return render(request, "newapp/question_detail.html",{"questions":question})

def question_new(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.published_date = timezone.now()
            question.save()
            return redirect("question_detail",pk=question.pk)
    else:
        form = QuestionForm()
    return render(request, "newapp/question_edit.html",{"form":form} )

def question_edit(request,pk):
    question = get_object_or_404(Question,pk=pk)
    if request.method == "POST":
        form = QuestionForm(request.POST,instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.published_date = timezone.now()
            question.save()
            return redirect("question_detail",pk=question.pk)
    else:
        form = QuestionForm(instance=question)
    return render(request, "newapp/question_edit.html",{"form":form} )
    
    
