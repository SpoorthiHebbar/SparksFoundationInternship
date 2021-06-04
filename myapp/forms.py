from django import forms
from django.http import request
from .models import Transaction
from myapp import models

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['sender','reciever','amount']

    def __init__(self,*args,**kwargs):
        
        super(TransactionForm,self).__init__(*args,**kwargs)
        self.fields['reciever'].empty_label = 'Select'
