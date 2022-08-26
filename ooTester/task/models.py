from django.db import models
from django import forms
from django.forms import ModelForm, NumberInput,TextInput

# Create your models here.
class Question(models.Model):
    text = models.CharField(max_length=250)
    photo = models.ImageField(upload_to='images/',null=True)
    is_complete = models.BooleanField(null=True)

    def __str__(self):
        return self.text

class UserDB(models.Model):
    name = models.CharField(max_length=100,null=True)
    age  = models.IntegerField(null=True)

    def __str__(self):
        return self.name

class User(forms.Form):
    name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'name':'username','placeholder':'Your Name ','style':'width: 300px','class':'form-control'}))
    age = forms.IntegerField(label="Your Age",min_value=6,widget=forms.NumberInput(attrs={'name':'age','placeholder':'Your Age ','style':'width: 300px','class':'form-control'}))
