from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')
def sum(request):
    n1 = int(request.POST['num1'])
    n2 = int(request.POST['num2'])
    name = request.POST['name']


    res = n1 + n2
    return render(request, 'result.html', {'result':res, 'name':name})