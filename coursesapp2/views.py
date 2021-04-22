from django.shortcuts import render , HttpResponse , redirect 
from django.contrib import messages
from coursesapp2.models import *

def index(request):
    context = {
        "courses" : Course.objects.all(),
        "descs" : Description.objects.all()
    }
    return render(request, "index.html",context)
def create(request):
    errors = Course.objects.basic_validator(request.POST)
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect("/courses")
    else:
        desc= Description.objects.create(desc=request.POST['desc'])
        name = Course.objects.create(name=request.POST['name'])
        
        return redirect("/courses")

def edit(request,id):
    context = {
        "id" : id,
        "course" : Course.objects.get(desc_id=id)
    }      
    return render(request,"edit.html", context)

def destroy(request,id):
    Course.objects.get(desc_id=id).delete()
    return redirect("/courses")

def comments(request,id):
    course2=Course.objects.get(desc_id=id)
    comment=course2.comments.all()
    
    context = {
        "id" : id,
        "course2":course2,
        "course" : Course.objects.get(desc_id=id),
        "comments": comment,
        
    }      
    return render(request,"comments.html", context)
def commcreate(request,id):
    course=Course.objects.get(desc_id=id)
    course.comments.comment=request.POST['comment']
    return redirect("/course/comments/"+str(id))



