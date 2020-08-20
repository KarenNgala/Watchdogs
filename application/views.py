from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    return render(request, 'index.html')

def neighbour(request):
    return render(request, 'neighbourhood.html')