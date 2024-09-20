from django.http import HttpResponse
from django.shortcuts import render
'''
# Accessing file path
import pathlib

this_dir = pathlib.Path(__file__)
this_dir_resolve = this_dir.resolve()
this_dir_resolve_parent = this_dir_resolve.parent
this_dir_resolve_parent = this_dir.parent

# Accessing html python way
def home(request, *args, **kwargs):
    html_ = "<h1>I am at home view</h1>"
    print(this_dir)
    print(this_dir_resolve)
    print(this_dir_resolve_parent)
    html_file_path = this_dir / "home.html"
    # html_ = html_file_path.read_text()
    return HttpResponse(html_)
    # return HttpResponse("<h1>Hello World</h1>")
    # return ("<h1>Hello World</h1>")
'''

'''
This is exactly the same function as the above one with 
1 differnece as 
request.user, 
request.method, 
request.user.is_authenticated

def new_home(request, *args, **kwargs):
    html_template = "base.html"
    context = {
        'title' : "My Title"
    }
    return render(request, html_template, context)
'''

'''
This explains the Django Template engine, 
how html templates are defined inside the views.py 
& settings.py file. 
Template inheritance & its extension to replace/add the
new code. 

def new_home(request, *args, **kwargs):
    html_template = "home.html"
    context = {
        'title' : 'Saas'
    }
    return render(request, html_template, context)
'''
from visits.models import PageVisit
def page_visit(request):
    return about_visit(request)

def about_visit(request):
    html_template = 'home.html'
    # print(request.path)
    PageVisit.objects.create(page_visit=request.path)
    total_page = PageVisit.objects.all()
    home_page = PageVisit.objects.filter(page_visit=request.path)
    try:
        percent = (home_page.count()/total_page.count())*100
    except:
        percent = 0
    context = {
        'title' : 'Saas',
        'page_count' : home_page.count(),
        'page_percent' : percent,
        'total_page_count' : total_page.count(),
    }
    return render(request, html_template, context)