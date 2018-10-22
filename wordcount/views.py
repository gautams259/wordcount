from django.http import HttpResponse
from django.shortcuts import render
def homepage(request):
   #return HttpResponse('<h1>this is homepage</h1>')
   return render(request,'home.html',{'name':'hi deepak'})

def contact(request):
   return HttpResponse('<h1>contact page</h1><br> this is our contact page')


def page2(request):
     return HttpResponse('<h2>WELCOME TO PAGE2</h2>')

def count(request):
    data=request.GET['textarea']
    print(data)
    l=data.split()
    print(l)
    return render(request,'count.html',{'ful':data})

def about(request):
	return render(request,'about.html')
