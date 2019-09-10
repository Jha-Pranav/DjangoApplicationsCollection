from django.shortcuts import render
# from django.http import HttpRequest, Http404
from .models import Questions, Choices

# Create your views here.

def index(response):
    return render(response, 'index.html')

def detail(response, question_id):
    return render(response, 'details.html')

def result(response, question_id):
    return render(response, 'result.html')








