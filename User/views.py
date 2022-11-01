from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import NewUser
from .models import User


def user_home(request):
    data = User.objects.all()
    usr = {'user_data': data}
    return render(request, 'User/user_home.html', usr)


def new_user(request):
    form = None
    if request.method == "GET":
        form = NewUser()
    elif request.method == "POST":
        form = NewUser(request.POST)
        if form.is_valid():
            new_user_form = User(first_name=form.cleaned_data["first_name"],
                                 middle_name=form.cleaned_data["middle_name"],
                                 last_name=form.cleaned_data["last_name"],
                                 street_address=form.cleaned_data["street_address"],
                                 city=form.cleaned_data["city"],
                                 state=form.cleaned_data["state"],
                                 zip=form.cleaned_data["zip"],
                                 country=form.cleaned_data["country"],
                                 phone_number=form.cleaned_data["phone_number"])

            new_user_form.save()
            return HttpResponseRedirect(f"/user")
    return render(request, "User/new_user.html", {'form': form})


def deactivate_user(request, id):
    all_data = User.objects.get(pk=id)
    if all_data.active == 'Y':
        all_data.active = 'N'
        all_data.save()
    else:
        all_data.active = 'Y'
        all_data.save()
    return HttpResponseRedirect(reverse('user_home'))
