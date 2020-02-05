import re

from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader, Context, Template

# Create your views here.
from django.template.context_processors import csrf


def test(request):
    # method 1
    t = loader.get_template('index.html')
    return HttpResponse(t.render({'name': 123}))

    # method 2    (Template and Context should use together)
    # t = Template('{{name}}')
    # c = Context({'name': 123})
    # return HttpResponse(t.render(c))

    # content of Context directory value can be common value, list, class


def course(request):
    t = loader.get_template('firstHTML.html')
    return HttpResponse(t.render())


def resume(request):
    t = loader.get_template('resume.html')
    return HttpResponse(t.render())


def submit_form(request):
    name = request.get['name']
    email = request.get['email']
    message = request.get['message']
    return HttpResponse("Succeed!" + name + '\n' + email + '\n' + message)


# def get_csrf(request):
#     # generate csrf and send to front-end
#     x = csrf(request)
#     csrf_token = x['csrf_token']
#     return HttpResponse('{} ; {}'.format(str(re), csrf_token))
