from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import Course

# Create your views here.
def index(request):
    context = {}
    context['course'] = Course.objects.all()
    return render(request,"courses_app/index.html",context)

def add(request):
    # course_name = request.POST['course_name']
    # desc = request.POST['desc']
    # y = {'course_name' : course_name,'desc':desc}
    errors = Course.objects.basic_validator(request.POST)
    if len(errors):
        for tag,error in errors.iteritems():
            messages.error(request,error,extra_tags=tag)
        return redirect('/')
    else:
        Course.objects.create(course_name = request.POST['course_name'], desc = request.POST['desc'])
        return redirect('/')

def destroy(request,id):
    context = {}
    context['course_id'] = Course.objects.get(id = id)

    print "contextiss-------{}".format(context['course_id'])
    return render(request,"courses_app/delete.html",context)

def delete(request,id):
    b = Course.objects.get(id = id)
    b.delete()
    return redirect('/')