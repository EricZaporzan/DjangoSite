from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import RequestContext, loader
from main.models import Blogpost

def index(request):
    title = "Home"
    template = loader.get_template('main/index.html')
    context = RequestContext(request, { 'title' : title })
    return HttpResponse(template.render(context))

def blog_overview(request):
    title = "Blog"
    blogposts = Blogpost.objects.order_by('-published')
    template = loader.get_template('main/blog_overview.html')
    context = RequestContext(request, { 'title' : title, 'blogposts' : blogposts })
    return HttpResponse(template.render(context))

def blog_details(request, blog_id):
    try:
        detail_post = Blogpost.objects.get(post_id=blog_id)
        title = detail_post.title
        template = loader.get_template('main/blog_details.html')
        context = RequestContext(request, { 'title' : title, 'detail_post' : detail_post })
        return HttpResponse(template.render(context))
    except Blogpost.DoesNotExist:
        raise Http404