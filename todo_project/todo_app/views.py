
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, "todo_app/index.html")
def about(request):
    return render(request, "todo_app/about.html")

# Create your views here.
