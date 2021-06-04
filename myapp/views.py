from django import forms
from myapp.forms import TransactionForm
from django.shortcuts import redirect, render, HttpResponse
from .models import Customer, Transaction
from .forms import TransactionForm
from myapp import models

def index(request):
    return render(request,"index.html")


def transaction(request,cust_id):
    if request.method =="GET":
        form = TransactionForm(initial={'sender':cust_id})
        return render(request,"transactions.html",{'form':form})
    else:
        form = TransactionForm(request.POST)
        if form.is_valid():
            sender = models.Customer.objects.get(pk=request.POST.get('sender'))
            recv = models.Customer.objects.get(pk=request.POST.get('reciever'))
            amt = request.POST.get('amount')
            sender.balance -= float(amt)
            recv.balance += float(amt)
            sender.save()
            recv.save()
            form.save()
        return redirect('view_users')

def view_transactions(request):
    trans = Transaction.objects.all()
    context = {
        "Alltrans": trans
        }
    return render(request,"view_transactions.html",context)


def view_users(request):
    users = Customer.objects.all()
    context = {
        "Allusers":users
    }
    return render(request,"users.html",context)

