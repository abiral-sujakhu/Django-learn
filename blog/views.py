from django.shortcuts import render
from django.http import HttpResponse


posts=[
     {
          'author':'CoreyMS',
          'title':'Blog post 1',
          'content':'first post content',
          'date_posted':'1st Feb 2026'
     },
      {
          'author':'Avi',
          'title':'Blog post 2',
          'content':'second post content',
          'date_posted':'2nd Feb 2026'
     }

]

def home(request):
    context={
         'posts':posts
    }
    return render(request,'blog/home.html',context)

def about(request):
     return render(request,'blog/about.html',{'title':'ABOUT'})
