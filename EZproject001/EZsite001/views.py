from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader, Context, Template
from django.core.mail import send_mail

# Create your views here.
from django.template.context_processors import csrf

# use 2 ways to test how to use template and pass value
# content of Context directory value can be common value, list, class
from EZsite001 import models


def test(request):
    # method 1
    # t = loader.get_template('test.html')
    # return HttpResponse(t.render({'name': 123}))

    # method 2    (Template and Context should use together)
    # t = Template('{{name}}')
    # c = Context({'name': 123})
    # return HttpResponse(t.render(c))

    t = loader.get_template('test.html')
    return HttpResponse(t.render())


def course(request):
    t = loader.get_template('superHTML.html')
    return HttpResponse(t.render())


def resume_en(request):
    if request.method == "GET":
        return render(request, 'resume.html')
    elif request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        if name and email and message:
            request.session['name'] = name
            request.session['email'] = email
            request.session['message'] = message
            return redirect('/submit/')
        else:
            return render(request, 'resume.html')


def resume_cn(request):
    if request.method == "GET":
        return render(request, 'resume_cn.html')
    elif request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        if name and email and message:
            request.session['name'] = name
            request.session['email'] = email
            request.session['message'] = message
            return redirect('/submit/')
        else:
            return render(request, 'resume_cn.html')


def submit(request):
    name = request.session['name']
    email = request.session['email']
    message = request.session['message']
    res = send_mail(subject='Contact By My website: ' + name + '<' + email + '>',
                    message='Name:' + str(name) + '\n' + 'Email:' + str(email) + '\n' + 'Message:' + str(message),
                    from_email='ervinzhang319@gmail.com', recipient_list=['ervinzhang319@gmail.com'],
                    fail_silently=False)
    if res == 1:
        statusmessage = "Succeed!"
        messages.success(request, statusmessage)
    else:
        statusmessage = "Oops! Something wrong with internet or other reasons"
    t = loader.get_template('submit.html')
    return HttpResponse(t.render({'status': statusmessage, 'name': name, 'email': email, 'message': message}))


def cmd(request):
    if request.method == "GET":
        return render(request, 'cmd.html')
    elif request.method == "POST":
        input = request.POST.get('input')
        result_eval = lambda x: eval(x)
        return render(request, 'cmd.html', {'input': input, 'output': result_eval(input)})


def pkb(request):
    # a1 = {'title': 'python basic', 'p1': 'regex'}
    # models.forum.objects.create(**a1)
    article = models.forum.objects.get(id=1)
    return render(request, 'pkb.html', {'article': article})


def webDev(request):
    t = loader.get_template('WebDev.html')
    return HttpResponse(t.render())


def quickatt(request):
    t = loader.get_template('quickatt.html')
    return HttpResponse(t.render())


def pythonspec(request):
    t = loader.get_template('PythonSpec.html')
    return HttpResponse(t.render())
