from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewList
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required


def home(response):
    return render(response, "main/home.html", {})


def home_login(response):
    return render(response, "main/home_login.html", {})


def base_login(response):
    return render(response, "main/base_login.html", {})


def galerija(response):
    return render(response, "main/galerija.html", {})


def pasirodymai(response):
    return render(response, "main/pasirodymai.html", {})


def apie_mus(response):
    return render(response, "main/apie_mus.html", {})


def vip(response):
    return render(response, "main/vip.html", {})

def duombaze(response):
    return render(response, "main/duombaze.html", {})

def vip_kalendorius(response):
    return render(response, "main/vip_kalendorius.html", {})

def iranga(response):
    return render(response, "main/iranga.html", {})


def index(response, id):
    ls = ToDoList.objects.get(id=id)

    print(ls.id)

    if ls in response.user.todolist.all():
        if response.method == "POST":
            if response.POST.get("save"):
                for item in ls.item_set.all():
                    if response.POST.get("c" + str(item.id)) == "clicked":
                        item.complete = True
                    else:
                        item.complete = False

                    item.save()

            elif response.POST.get("newItem"):
                txt = response.POST.get("new")

                if len(txt) > 2:
                    ls.item_set.create(text=txt, complete=False)
                else:
                    print("invalid")

        return render(response, "main/list.html", {"ls": ls})
    return render(response, "main/view.html", {})

