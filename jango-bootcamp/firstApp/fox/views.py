from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import Entry


def index(request):
    entry1 = Entry('Name1', 'This is the changed description for first block')
    entry2 = Entry('Name2', 'This is the changed description for second block')
    entry3 = Entry('Name3', 'This is the changed description for third block')
    entry_list = [entry1, entry2, entry3]
    return render(request, 'index.html', {'entry':entry_list})

def gallery(request):
    return render(request, 'pages/gallery.html')


