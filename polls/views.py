# /usr/bin/python
#coding:utf-8
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404
from django.template import RequestContext,loader
from models import Question
# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_data')[:5]

    #第二种方式
    #快捷方式：render()
    context = {'latest_question_list':latest_question_list}
    return render(request,'polls/index.html',context)


    #第一种方式
    #常见的习惯是载入一个模板、填充一个context 然后返回一个含有模板渲染结果的HttpResponse对象
    # template = loader.get_template('polls/index.html')
    # context = RequestContext(request,{
    #     'latest_question_list':latest_question_list
    # })
    # return HttpResponse(template.render(context))


def detail(request,question_id):

    #第二种404错误处理
    #快捷方式：get_object_or_404()
    question = get_object_or_404(Question,pk=question_id)
    return render(request,'polls/detail.html',{'question':question})

    #第一种404错误处理
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exiest")
    # return render(request,'polls/detail.html',{'question':question})


def results(request,question_id):
    response = "Yo're looking at the result of question %s"
    return HttpResponse(response %question_id)

def vote(request,question_id):
    return HttpResponse("You're voting on question %s" %question_id)

