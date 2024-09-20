from django.shortcuts import render, get_object_or_404, redirect 
from .models import TeamInfo, User, Player, Waiver 
from .forms import PlayerFormSet, TeamForm, UserForm, WaiverForm
from django.contrib import messages 
from rest_framework.response import Response 
from rest_framework import status 
from rest_framework.decorators import api_view
from rest_framework.decorators import APIView 


def home(request):
    home_content = {"home": "Welcome to Home Page! Enjoy your game"}
    return render(request, "home.html", home_content)

def about(request):
    about_content = {"about": "This is about page"}
    return render(request, "about.html", about_content)

def add_team(request):
    if request.method == "POST":
        form = TeamForm(request.POST)
        if form.is_valid():
            team_name = form.cleaned_data['team_name']
            form.instance.team_name = team_name.capitalize()
            form.save()
            messages.success(request, "Add Team Info successfully.")
    else:
        form = TeamForm()
    return render(request, 'team.html', {'form': form})

def add_user(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            co_last_name = form.cleaned_data['co_last_name']
            co_first_name = form.cleaned_data['co_first_name']
            form.instance.first_name = first_name.capitalize()
            form.instance.last_name = last_name.capitalize()
            co_first_name = co_first_name.capitalize()
            co_last_name = co_last_name.capitalize()
            form.save()
            messages.success(request, "Add user successfully.")
    else:
        form = UserForm()
    return render(request, 'user.html', {'form': form})


def add_players(request):
    if request.method == "POST":
        form = PlayerFormSet(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            form.instance.first_name = first_name.capitalize()
            form.instance.last_name = last_name.capitalize()
            form.save()
            messages.success(request, "Add player successfully.")
    else:
        form = PlayerFormSet()
    return render(request, 'addPlayer.html', {'form': form})

def waiver(request):
    if request.method == "POST":
        form = WaiverForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            form.instance.first_name = first_name.capitalize()
            form.instance.last_name = last_name.capitalize()
            form.save()
            messages.success(request, "Waiver has been completed")
    else:
        form = WaiverForm()
    return render(request, 'waiver.html', {'form': form})

def team(request):
    team_data = TeamInfo.objects.all()
    user_data = User.objects.all()
    player_data = Player.objects.all()
    context = {'team': team_data, 'user': user_data, 'player': player_data}
    return render(request, 'signUp.html', context)

def display_single_team(request, pk=None):
    team_data = get_object_or_404(TeamInfo, pk=pk)
    return render(request, 'single_team.html', {'single_team': team_data })
    

