from django.shortcuts import render
from django.template.loader import render_to_string
import datetime,calendar
from django.http import HttpResponse
from django import forms
from django.contrib.auth.models import User
# Create your views here.
def crudops(request):
    #creating an entry

    #Reading all entries
    res="printing all objects in DB:<br>"
    return HttpResponse(res+'bjhgbjh')
def hello(request):
    cal_tuple=calendar.TextCalendar(calendar.SUNDAY)
    weekdays=['SUN','MON','TUE','WED','THU','FRI','SAT']
    cal=cal_tuple.formatmonth(2019,11)
    day = datetime.datetime.now().date()
    return render(request,'hello.html',{'day':day,'name':'Ravikirana B','cal_disp':cal,'weekdays':weekdays,'name1':'GOVARDHANA GOWDA G R'})
def articlea(request,articleid):
    text='Displaying article number : %s' %articleid
    return HttpResponse(text)
def article(request,month,year):
    text="Displaying article number : %s-%s"%(month,year)
    return HttpResponse(text)
def home(request):
    return render(request,'home.html')
def add(request):
    val1=request.POST['num1']
    val2=request.POST['num2']
    res=val1+val2
    print('add request method:',request.method)
    return render(request,"result.html",{'result': res})