from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Plans
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


def plans_index(request):
    plans = Plans.objects.all()
    return render(request, "plan/index.html", {"plans": plans})


def plans_detail(request, plan_id):
    plan = Plans.objects.get(id=plan_id)
    return render(request, "plan/detail.html", {"plan": plan})


def plans_create(request):
    return render(request, "plan/create.html")


def main_page(request):
    return render(request, "main-page.html")


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)
