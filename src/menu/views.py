from django.shortcuts import render
from django.views.generic import TemplateView


def home(request):
    return render(request, 'tree_menu/home.html')

def about(request):
    return render(request, 'tree_menu/about.html')

def team(request):
    return render(request, 'tree_menu/team.html')

def history(request):
    return render(request, 'tree_menu/history.html')

def contact(request):
    return render(request, 'tree_menu/contact.html')