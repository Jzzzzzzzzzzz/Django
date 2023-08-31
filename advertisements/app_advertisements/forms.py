from django import forms
from django.forms import ModelForm
from .models import *
from django.core.exceptions import ValidationError
class AdvertisementForm(forms.ModelForm):
    #title = forms.CharField(max_length=64,widget=forms.TextInput(attrs={"class":"form-control form-control-lg"}))
    #Описание = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control form-control-lg"}))
    #price = forms.DecimalField(widget=forms.NumberInput(attrs={"class":"form-control form-control-lg"}))
    #negotiable = forms.BooleanField(widget=forms.CheckboxInput(attrs={"class":"form-check-input "}),required=False)
    #image = forms.ImageField(widget=forms.FileInput(attrs={"class":"form-control form-control-lg"}))
    class Meta:
        model = Advertisements
        fields = ["title","description","price","negotiable","image"]
        widgets = {
            'title': forms.TextInput(attrs={'class': "form-control form-control-lg maxlength=70"}),
            "description":forms.Textarea(attrs={"class":"form-control form-control-lg"}),
            "price":forms.NumberInput(attrs={"class":"form-control form-control-lg"}),
            "negotiable":forms.CheckboxInput(attrs={"class":"form-check-input "}),
            "image":forms.FileInput(attrs={"class":"form-control form-control-lg"})


        }


    def clean_title(self):
        t=self.cleaned_data["title"]
        symbol = ["?", "!", "&", "/", "."]
        if any(t.startswith(s) for s in symbol):
            raise ValidationError(
                'Заголовок не может начинаться с одного из следующих символов: {}'.format(", ".join(symbol)))
        else:return t













