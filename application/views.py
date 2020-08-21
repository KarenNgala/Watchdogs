from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from django.http import Http404

# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    return render(request, 'index.html')


def join(request):
    hoods = Neighbourhood.objects.all()
    return render(request, 'django_registration/registration_complete.html', {'hoods':hoods})

def join_btn(request, hood_id):
    selected_hood = Neighbourhood.objects.get(id=hood_id)
    if request.user.profile.hood == None:
        request.user.profile.hood = selected_hood
        request.user.profile.save()
        return redirect('home')
    else:
        alert('Bad request. You are already in a hood')