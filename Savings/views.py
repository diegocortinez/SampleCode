from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Savings
from User.models import User
from .forms import NewSavings


def savings_home(request):
    data_1 = User.objects.all()
    data_2 = Savings.objects.all()
    dta = {'user': data_1, 'savings': data_2}
    return render(request, 'Savings/savings_home.html', dta)


def new_savings(request):
    form = None
    if request.method == "GET":
        form = NewSavings()
    elif request.method == "POST":
        form = NewSavings(request.POST)
        if form.is_valid():
            new_savings_form = Savings(user_id=form.cleaned_data["user_id"],
                                       savings_balance=form.cleaned_data["savings_balance"],
                                       date_balance=form.cleaned_data["date_balance"])

            new_savings_form.save()
            return HttpResponseRedirect(f"/savings")
    return render(request, "Savings/new_savings.html", {'form': form})
