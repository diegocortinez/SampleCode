from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import NewChecking
from .models import Checking
from User.models import User


def checking_home(request):
    data_1 = User.objects.all()
    data_2 = Checking.objects.all()
    dta = {'user': data_1, 'checking': data_2}
    return render(request, 'Checking/checking_home.html', dta)


def new_checking(request):
    form = None
    if request.method == "GET":
        form = NewChecking()
    elif request.method == "POST":
        form = NewChecking(request.POST)
        if form.is_valid():
            new_checking_form = Checking(user_id=form.cleaned_data["user_id"],
                                         checking_balance=form.cleaned_data["checking_balance"],
                                         date_balance=form.cleaned_data["date_balance"])

            new_checking_form.save()
            return HttpResponseRedirect(f"/checking")
    return render(request, "Checking/new_checking.html", {'form': form})
