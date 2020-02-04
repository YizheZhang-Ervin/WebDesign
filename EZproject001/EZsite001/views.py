from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader, Context, Template


# Create your views here.


def index(request):
    # method 1
    t = loader.get_template('index.html')
    return HttpResponse(t.render({'name': 123}))

    # method 2    (Template and Context should use together)
    # t = Template('{{name}}')
    # c = Context({'name': 123})
    # return HttpResponse(t.render(c))

    # content of Context directory value can be common value, list, class


def home(request):
    t = loader.get_template('firstHTML.html')
    return HttpResponse(t.render())


def blog(request):
    t = loader.get_template('blog.html')
    return HttpResponse(t.render())
