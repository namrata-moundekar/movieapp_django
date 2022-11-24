from rest_framework.routers import SimpleRouter
from movie_app.views import *

simple = SimpleRouter()

simple.register('movie',MovieCrud)
simple.register('actor',ActorCrud)
simple.register('genres',GenresCrud)

urlpatterns = simple.urls