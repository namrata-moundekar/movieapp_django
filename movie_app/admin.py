from django.contrib import admin
from movie_app.models import Movie,Actor,Genres

# Register your models here.
admin.site.register(Movie)
admin.site.register(Actor)
admin.site.register(Genres)