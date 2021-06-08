from django.db.models.fields import DateField
from django.shortcuts import render, redirect
from .models import Show
from datetime import datetime

def index(request):
    return redirect('/shows')

def shows(request):
    context = {
        "all_shows": Show.objects.all()
    }
    return render(request, "shows.html", context)

def show_details(request, id):      # easy thing to miss is include the "id" here, along with request. If 'id' is in URLs.py, needs to be here in views too
    context = {
        "show": Show.objects.get(id=id),
    }
    return render(request, "show_details.html", context)

def edit(request, id):
    context = {
            "show": Show.objects.get(id=id),
        }
    return render(request, "edit.html", context)

def update(request, id):
    if request.method == "POST":
        instance = Show.objects.get(id=id)      # use 'id' from urls.py; could also embed a hidden field into html form to make work
        instance.title=request.POST['title']
        instance.network=request.POST['network']
        # originally I had 'release_date' on form set up as text, not "date", which means the request.POST came through as string, not date object
        # This meant I had to bring it into a variable and then convert that string variable into a date object as follows: 
        # rawdate=request.POST['release_date']   # use variable 'rawdate' as the string version from POST request
        # objdate=datetime.strptime(rawdate, '%Y-%m-%d') # use datetime.strptime() method to convert string version to object version of date
        instance.release_date=request.POST['release_date'] # because by 'release_date' is not set up as "date" on form, I can just assign it directly
        instance.description=request.POST['description']
        instance.save()
    
    return redirect(f'/shows/{id}')


def destroy(request, id):   # ibid on include the "id" here
    instance = Show.objects.get(id=id)      # instantiate
    instance.delete()                       # delete

    return redirect('/')

def new(request):

    return render(request, "new.html")

def create(request):
    if request.method == "POST":
        Show.objects.create(title=request.POST['title'], network=request.POST['network'], release_date=request.POST['release_date'], description=request.POST['description'])
    instance = Show.objects.get(title=request.POST['title'])

    return redirect(f'/shows/{instance.id}')


# Create your views here.
