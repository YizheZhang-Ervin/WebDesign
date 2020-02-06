import re

from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader, Context, Template
from django.core.mail import send_mail

# Create your views here.
from django.template.context_processors import csrf


# use 2 ways to test how to use template and pass value
# content of Context directory value can be common value, list, class
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


def resume(request):
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
            return redirect('/submit_form/')
        else:
            return render(request, 'resume.html')


def submit_form(request):
    name = request.session['name']
    email = request.session['email']
    message = request.session['message']
    res = send_mail(subject='Contact By My website: ' + name + '<' + email + '>',
                    message='Name:'+str(name) + '\n' + 'Email:' + str(email) + '\n' + 'Message:' + str(message),
                    from_email='ervinzhang319@gmail.com', recipient_list=['ervinzhang319@gmail.com'],
                    fail_silently=False)
    if res == 1:
        statusmessage = "Succeed!"
    else:
        statusmessage = "Oops! Something wrong with internet or other reasons"
    return HttpResponse(statusmessage + name + '\n' + email + '\n' + message)

# get csrf from back-end
# def get_csrf(request):
#     # generate csrf and send to front-end
#     x = csrf(request)
#     csrf_token = x['csrf_token']
#     return HttpResponse('{} ; {}'.format(str(re), csrf_token))


# login/redirect/logout
# def login(request):
#     if request.method == "GET":
#         return render(request, 'login.html')
#     elif request.method == "POST":
#         user = request.POST.get('user')
#         pwd = request.POST.get('pwd')
#         if user == 'root' and pwd == "123123":
#             # Generate random string
#             # Write to user browser cookie
#             # Saved in server session
#             # Set related content in the dictionary corresponding to random string
#             request.session['username'] = user
#             request.session['islogin'] = True
#             if request.POST.get('rmb', None) == '1':
#                 # setting timeout
#                 request.session.set_expiry(10)
#             return redirect('/index/')
#         else:
#             return render(request, 'login.html')
#
#
# def index(request):
#     # Get the current random string
#     # Get the corresponding information according to the random string
#     if request.session.get('islogin', None):
#         return render(request, 'index.html', {'username': request.session['username']})
#     else:
#         return HttpResponse('please login ')
#
#
# def logout(request):
#     del request.session['username']
#     request.session.clear()
#     return redirect('/login/')
