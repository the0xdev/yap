# SPDX-FileCopyrightText: 2025 Imran Mustafa <imran@imranmustafa.net>
#
# SPDX-License-Identifier: GPL-3.0-or-later

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import aauthenticate, login, logout
from django.contrib import messages

from django.contrib.auth.models import User



from app.forms import PasteForm
from app.models import Paste

def index(request):
    pastes = Paste.objects.all().order_by('-time_created')[:17]
    match request.method:
        case "GET":
            return render(request, "index.html", {"form": PasteForm(), "pastes": pastes})
        case "POST":
            form = PasteForm(request.POST)
            if form.is_valid():
                print(form.cleaned_data.get("id"))
                new_paste = form.save(commit=False)
                new_paste.author = request.user
                new_paste.save()

                return redirect("paste", id=new_paste.id)
            else:
                return render(request, "index.html", {"form": form, "pastes": pastes})

def paste(request, id):
    paste = Paste.objects.get(id=id)
    return render(request, "paste.html", {"paste": paste})

def signup(request):
    match request.method:
        case "GET":
            return render(request, "registration/signup.html", {"form": UserCreationForm()})
        case "POST":
            form = UserCreationForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                messages.success(request, f"Welcome to YAP {form.cleaned_data.get('username')}")
                return redirect("index")
            else:
                messages.error(request, f"could not rigistar user")
                return render(request, "registration/signup.html", {"form": form})
        case _:
            return 405

@login_required()
def account(request):
    user = User.objects.get(username=request.user.username)
    pastes = Paste.objects.filter(author=user)
    return render(request, "account.html", {"user": user, "pastes": pastes})

def profile(request, username):
    user = User.objects.get(username=username)
    pastes = Paste.objects.filter(author=user).order_by('-time_created')
    return render(request, "profile.html", {"user": user, "pastes": pastes})
