from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Question, Choice
from django.views import generic

# Create your views here.

def index(response):
    latest_questions = Question.objects.all()
    
    return render(response, 'Pool/index.html', context={'question_list' : latest_questions})

#class based views
class IndexView(generic.ListView):
    template_name = 'Pool/index.html'
    context_object_name = 'question_list'

    def get_queryset(self):
        "Return all questions"
        return Question.objects.all()

def details(response, question_id):
    question = get_object_or_404(Question, pk=question_id)   
    return render(response, 'Pool/detail.html', context={'question_detail': question})


class DetailsValue(generic.DetailView):
    model = Question
    template_name='Pool/detail.html'
    context_object_name = 'question_detail'


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'Pool/result.html', {'question':question})


class ResultView(generic.DetailView):
    model = Question
    template_name = 'Pool/result.html'
    context_object_name = 'question'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError,):
        return render(request, 'Pool/detail.html', {'question_detail': question,
            'error_message': "You didn't selected a choice"})

    selected_choice.votes += 1
    selected_choice.save()

    return HttpResponseRedirect(reverse('pools:result', args=(question_id,)))

    
    








