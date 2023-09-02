from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def home_page(request):
    return render(request, 'base_layout.html', {})


@login_required()
def dashboard(request):
    return render(request, 'profiles/dashboard.html', {})


def register(request):
    pass
