from django import forms
from django.forms import ModelMultipleChoiceField, SelectMultiple, TextInput,Textarea
from PeliculasDeCulto.models import Category, PeliculasDeCulto

# class PeliculasDeCultoCreateForm(forms.Form):
#     title = forms.CharField(label="Culto Name",
#                             widget=forms.TextInput(attrs={"class":"form-control"})
#                             )
#     description = forms.CharField(label="Culto Description", widget=forms.Textarea(attrs={"class":"form-control"}))
#     date = forms.DateField(widget=forms.TextInput(attrs={"class":"form-control"}))
#     imageUrl = forms.CharField( widget=forms.TextInput(attrs={"class":"form-control"}))
#     slug = forms.SlugField( widget=forms.TextInput(attrs={"class":"form-control"}))

class PeliculasDeCultoCreateForm(forms.ModelForm):
    class Meta:
        model = PeliculasDeCulto
        fields = ('__all__')
        labels = {
            'title':"Culto Name",
            'description':"Culto Description",
            'date':"Movie date: dd-mm-yyyy",
            'slug':"Slug: peliculas-de-culto",
            'isActive':"Want to publish?",
            'isHome':"Want to see Home Page?"
            
        }
        widgets = {
            "title":TextInput(attrs={"class":"form-control"}),
            "description":Textarea(attrs={"class":"form-control"}),
            "date":TextInput(attrs={"class":"form-control"}),
            "slug":TextInput(attrs={"class":"form-control"}),
        }

class PeliculasDeCultoEditForm(forms.ModelForm):
    class Meta:
        model = PeliculasDeCulto
        fields = ('title','description','imageUrl','slug','categories','isActive')
        labels = {
            'title':"Culto Name",
            'description':"Culto Description",
            'date':"Movie date: dd-mm-yyyy",
            'slug':"Slug: peliculas-de-culto",
            'isActive':"Want to publish?",
            'isHome':"Want to see Home Page?"
            
        }
        widgets = {
            "title":TextInput(attrs={"class":"form-control"}),
            "description":Textarea(attrs={"class":"form-control"}),
            "date":TextInput(attrs={"class":"form-control"}),
            "slug":TextInput(attrs={"class":"form-control"}),
            "categories": SelectMultiple(attrs={"class":"form-control"})
        }