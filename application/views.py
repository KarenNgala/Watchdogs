from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from .forms import UserRegisterForm,UserUpdateForm,BusinessForm,UpdateProfileForm, NeighbourHoodForm, PostForm
from .models import Neighbourhood, Profile, Business, Post 
# Create your views here.

posts = [
    {
        'author': 'Bryson',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2020'
    }
]

def register(request):
    if request.method == 'POST':#post request
        form = UserRegisterForm(request.POST)#new form that has data within request.POST
        if form.is_valid():#makes sure data gotten is valid when submitted
            form.save()#this will save the data 
            username = form.cleaned_data.get('username')#
            messages.success(request, f'Your account has been created and Your now logged into the app!')
            return redirect('login')#accounts/register/complete/
    else:#if its not successful then it will display the same page again
        form = UserRegisterForm()
    return render(request, 'django_registration/registration_form.html' ,{'form':form})



@login_required(login_url='/accounts/login/')
def home(request):
    return render(request, 'index.html')

@login_required
def profile(request):    
    return render(request, 'registration/profile.html')

def business(request):
    context = {
        'post':posts
    }
    return render(request, 'business.html', context)

def neighbourhoods(request):
    all_hoods = Neighbourhood.objects.all()
    all_hoods = all_hoods[::-1]
    params = {
        'all_hoods': all_hoods,
    }
    return render(request, 'neighbourhoods.html', params)

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

def join_neighbourhood(request, id):
    neighbourhood = get_object_or_404(Neighbourhood, id=id)
    request.user.profile.neighbourhood = neighbourhood
    request.user.profile.save()
    return redirect('hood')

def leave_neighbourhood(request, id):
    hood = get_object_or_404(Neighbourhood, id=id)
    request.user.profile.neighbourhood = None
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