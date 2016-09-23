# /usr/bin/python
#coding:utf-8
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.template import RequestContext,loader
from django.core.urlresolvers import reverse
from models import Question,Choice
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
    question = get_object_or_404(Question,pk=question_id)
    return render(request,'polls/results.html',{'question':question})
    response = "Yo're looking at the result of question %s"
    return HttpResponse(response %question_id)

def vote(request,question_id):
    p = get_object_or_404(Question,pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except(KeyError,Choice.DoesNotExist):
        return render(request,'polls/detail.html',
                      {'question':p,
                       'error_message':"you don't select a choice"
                      })
    else:
        selected_choice.votes += 1
        selected_choice.save()
    return HttpResponseRedirect(reverse('polls:results',args=(p.id,)))
    #在增加Choice的得票数之后，代码返回一个 HttpResponseRedirect而不是常用的HttpResponse。HttpResponseRedirect只接收一个参数：用户将要被重定向的URL
    #在这个例子中，我们在HttpResponseRedirect的构造函数中使用reverse()函数。这个函数避免了我们在视图函数中硬编码URL。它需要我们给出我们想要跳转的视图的名字和该视图所对应的URL模式中需要给该视图提供的参数。 在本例中，使用在教程3中设定的URLconf， reverse() 调用将返回一个这样的字符串：
    #'/polls/3/results/'
    # return HttpResponse("You're voting on question %s" %question_id)

