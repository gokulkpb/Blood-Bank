from django.shortcuts import redirect, render
from .models import person
from django.contrib.auth.models import User, auth
from django.contrib import messages

def home(request):
    if 'username' in request.session:
        return redirect('display')
    else:
        return render(request, 'login.html')
    
def signup(request):
    if 'username' in request.session:
        return redirect('display')
    elif request.method == 'POST':
       fname = request.POST['fname']
       lname = request.POST['lname']
       user = request.POST['user']
       email = request.POST['email']
       password = request.POST['pswd']
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
    if 'username' not in request.session:
        return redirect('login')
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
    if 'username' in request.session:
        return redirect('display')
    elif request.method == 'POST':
        username = request.POST['user']
        passw = request.POST['password']
        
        user = auth.authenticate(username = username, password = passw)

        if user is not None:
            request.session['username'] = username
            request.session['Name'] = user.first_name
            #auth.login(request, user)
            return redirect('display')
        else:
            messages.info(request, 'Credentials not found!')
            return redirect('login')
    else:
        return render(request, 'login.html')
     


def display(request):
    if 'username' in request.session:
        lst = person.objects.all()
        return render(request, 'display.html', {'lst':lst})
    else:
        return redirect('login')

def logout(request):
    if 'username' in request.session:
        request.session.flush()
    return redirect('/')
        
