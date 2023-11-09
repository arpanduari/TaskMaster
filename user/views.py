from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm

# Create your views here.


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Welcom {username} to TaskMaster")
            return redirect("login")
    else:
        form = RegisterForm()
    return render(request, "user/register.html", context={"form": form})
