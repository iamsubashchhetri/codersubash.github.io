from django.contrib.auth.models import User
from django.shortcuts import render,HttpResponse,redirect
from home import models
# Create your views here.
def home(request):
 #return HttpResponse('this is home')
 return render(request, 'home.html')

def contact(request):
 if request.method=="POST":
   name=request.POST['name']
   email=request.POST['email']
   message=request.POST['message']
   ins = models.Contact(name=name, message=message, email=email)
   ins.save()
   print("your data has been saved to db")
 return render(request, 'contact.html')
  
def about(request):
 #return HttpResponse('<h1>Page was found</h1>')
 return render(request, 'about.html')
   
def login(request):
 #return HttpResponse('<h1>Page was found</h1>')
 return render(request, 'login.html')

def signup(request):
    if request.method =='POST':
        username = request.POST['username']
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        email = request.POST['email_id']
        password = request.POST['pass']

        x=User.objects.create_user(username=username,first_name=firstname,last_name=lastname,email=email,password=password)
        x.save()
        print("user created")
        return redirect('/')
    else:
     return render(request, 'signup.html')
  
def blog(request):
 #return HttpResponse('<h1>Page was found</h1>')
 return render(request, 'blog.html')
 
