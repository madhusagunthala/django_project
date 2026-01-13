from django.shortcuts import render
from .models import*
# Create your views here.

def index(request):
    arts=article1.objects.all()
    pics=article2.objects.all()
    return render(request,'index.html',{
        'arts': arts,
        'pics':pics
        })