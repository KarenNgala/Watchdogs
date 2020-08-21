from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from .forms import *
from django.http import Http404
from .models import *

# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    current_hood = request.user.profile.hood
    posts = Post.objects.filter(neighborhood=current_hood.id).all()
    if current_hood == None:
        return redirect('complete')
    else:
        showing = Neighbourhood.objects.get(id=current_hood.id)
    return render(request, 'index.html', {'hood':showing, 'posts':posts})


@login_required(login_url='/accounts/login/')
def profile(request):    
    return render(request, 'registration/profile.html')


def business(request):
    current_hood = request.user.profile.hood
    business = Business.objects.filter(neighborhood=current_hood.id).all()
    return render(request, 'business.html', {'business':business})


def create_neighbourhood(request):
    if request.method == 'POST':
        form = NeighbourHoodForm(request.POST, request.FILES)
        if form.is_valid():
            hood = form.save(commit=False)
            hood.admin = request.user.profile
            hood.save()
            return redirect('hood')
    else:
        form = NeighbourHoodForm()
    return render(request, 'newhood.html', {'form': form})


def leave_neighbourhood(request):
    request.user.profile.hood = None
    request.user.profile.save()
    return redirect('hood')


def single_neighbourhood(request, hood_id):
    hood = Neighbourhood.objects.get(id=hood_id)
    business = Business.objects.filter(neighbourhood=hood)
    posts = Post.objects.filter(hood=hood)
    posts = posts[::-1]
    if request.method == 'POST':
        form = BusinessForm(request.POST)
        if form.is_valid():
            b_form = form.save(commit=False)
            b_form.neighbourhood = hood
            b_form.user = request.user.profile
            b_form.save()
            return redirect('single-hood', hood.id)
    else:
        form = BusinessForm()
    params = {
        'hood': hood,
        'business': business,
        'form': form,
        'posts': posts
    }
    return render(request, 'single_hood.html', params)

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