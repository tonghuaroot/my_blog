from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.template.loader import get_template
from datetime import datetime
from django.shortcuts import redirect

# Create your views here.
def homepage(request):
    templates = get_template('index.html')
    posts = Post.objects.all()
    now = datetime.now()
    html = templates.render(locals())
    return HttpResponse(html)

def navigation(request):
    templates = get_template('navigation.html')
    now = datetime.now()
    html = templates.render(locals())
    return HttpResponse(html)

def showpost(request,slug):
    template = get_template('post.html')
    try:
        post = Post.objects.get(slug=slug)
        if post != None:
            html = template.render(locals())
            return HttpResponse(html)
    except:
        return redirect('/')
