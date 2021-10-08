from django.shortcuts import redirect, render
from .models import person
from django.contrib.auth.models import User, auth
from django.contrib import messages

def home(request):
    return render(request, 'login.html')
    
def signup(request):
    if request.method == 'POST':
       fname = request.POST['fname']
       lname = request.POST['lname']
       user = request.POST['user']
       email = request.POST['email']
       password = request.POST['password']
       if User.objects.filter(username = user).exists():
           messages.info(request, 'Username already exists!')
           return redirect('signup')
       elif User.objects.filter(email = email).exists():
           messages.info(request, 'Email already exists!')
           return redirect('signup')
       else: 
            user = User.objects.create_user(username = user, password = password, email = email, first_name = fname, last_name = lname)
            user.save()
            print('user created ')
            return redirect('login')
    else:
        return render(request, 'signup.html')

#changed to add donor
def add_donor(request):
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        bg = request.POST['bg']
        mob = request.POST['mob']
        email = request.POST['email']
    
        details = person.objects.create(name = name, email = email, age = age, contact = mob, blood = bg, password = 'n')
        details.save()
        return redirect('display')
    else:
        return render(request, 'index.html')

def login(request):
    if request.method == 'POST':
        user = request.POST['user']
        passw = request.POST['password']
        
        user = auth.authenticate(username = user, password = passw)

        if user is not None:
            auth.login(request, user)
            return redirect('display')
        else:
            messages.info(request, 'Credentials not found!')
            return redirect('login')
    else:
        return render(request, 'login.html')
     


def display(request):
    return render(request, 'display.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
