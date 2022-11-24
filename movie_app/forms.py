from django.core import validators
from django import forms
from movie_app.models import Movie,Actor,Genres



class DateInput(forms.DateInput):
    input_type= 'date'

Demo_choices=[('p','p')]

class MovieForm(forms.ModelForm):
	class Meta:
		model = Movie
		fields = ['name', 'release_date', 'actors','poster_image','genres','rating']
	def __init__(self, *args, **kwargs):
		super(MovieForm, self).__init__(*args, **kwargs)
		
        


