from django.forms import ModelForm
from django import forms
from .models import Snake

class SnakeForm(forms.ModelForm):
    name = forms.CharField(
        label='Snake_Name',
        widget = forms.TextInput(attrs={'class': 'form-control'})
    )
    venomous = forms.BooleanField(
        label='Is venomous ?',
        widget = forms.CheckboxInput(),
        required=False)
    region = forms.ChoiceField(
        label='Snake_Region',        
        choices=(
        ('asia','Asia'),
        ('europa','Europa'),
        ('africa','Africa'),
        ('south_america','South America'),
        ('north_america','Nort America'))
    )


    class Meta:
        model = Snake
        fields =['name','description','color_pattern','favourite_prey','region','venomous']
        form_classes = {'class':'form-control'}
        widgets={
            'description':forms.TextInput(attrs=form_classes),
            'color_pattern':forms.TextInput(attrs=form_classes),
            'favourite_prey':forms.TextInput(attrs=form_classes),
            'region':forms.TextInput(attrs=form_classes)           
        }