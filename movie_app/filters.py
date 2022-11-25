from django import forms
# from django.contrib.auth.models import User, Group
from movie_app.models import Movie, Actor, Genres
import django_filters


class MovieFilter(django_filters.FilterSet):
    genres = django_filters.ModelMultipleChoiceFilter(queryset=Genres.objects.all(), widget=forms.CheckboxSelectMultiple)
    actors = django_filters.ModelMultipleChoiceFilter(queryset= Actor.objects.all())
    class Meta:
        model = Movie
        fields = ['genres','actors']