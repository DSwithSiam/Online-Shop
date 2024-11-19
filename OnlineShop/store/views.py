from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView, DeleteView

def Home(request):
    return render(request, 'store/index.html')