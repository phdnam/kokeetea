from django.shortcuts import render

# Create your views here.

# from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Question
from django.utils import timezone
from .forms import QuestionForm, AnswerForm


def question_create(request):
    """
    kokee  질문 등록
    """
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.save()
            return redirect('kokee:index')
    else:
         form = QuestionForm()
    context = {'form': form}
    return render(request, 'kokee/question_form.html', context)

def index(request):
    """
    kokee 목록 출력
    """
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list' : question_list}
    return render(request, 'kokee/question_list.html', context)
    return HttpResponse("안녕하세요? Kokeetea에 오신것을 환영합니다.")

def detail(request, question_id):
    """
    kokee 목록 출력
    """
    question = get_object_or_404(Question, pk=question_id)
    context = {'question' : question}
    return render(request, 'kokee/question_detail.html', context)

def answer_create(request, question_id):
    """
    kokee 답변 등록
    """
    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question  =question
            answer.save()
            return redirect('kokee:detail', question_id=question.id)
    else:
         form = AnswerForm()
    context = { 'question': question,'form': form}
    return render(request, 'kokee/question_detail.html', context)


"""
    question.answer_set.create(contents=request.POST.get('contents'),
                               create_date=timezone.now())
    return rediret('kokee:detail', question_id=question.id)
"""
