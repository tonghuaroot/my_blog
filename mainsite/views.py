from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.template.loader import get_template
from datetime import datetime

# Create your views here.
def homepage(request):
    templates = get_template('index.html')
    posts = Post.objects.all()
    now = datetime.now()
    html = templates.render(locals())
    '''
    post_list = list()
    for count,post  in enumerate(posts):
        post_list.append("No.{}".format(str(count)) + " " +str(post) + "<hr>")
        post_list.append("<small>" + str(post.body.encode('utf-8'))\
        + "</small><br><br>")
    '''
    return HttpResponse(html)
