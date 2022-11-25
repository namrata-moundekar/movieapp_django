from itertools import count

from django.shortcuts import render, redirect, HttpResponse
from movie_app.models import Movie, Actor, Genres
from movie_app.serializers import GenresSerializer, ActorSerializer, MovieSerializer, MovieApiSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view, permission_classes, renderer_classes
from rest_framework.response import Response
from rest_framework import status
from movie_app import serializers as serial
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from django.http import JsonResponse
from rest_framework.pagination import PageNumberPagination
from django.shortcuts import HttpResponse

from movie_app.filters import MovieFilter


# print(connection.queries)


###############################  UI OF MOVIE SHOWBOX   #####################################
def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 4
    page_size_query_param = 'page_size'
    max_page_size = 5


def search(request):
    user_list = Movie.objects.all()
    user_filter = MovieFilter(request.GET, queryset=user_list)
    return render(request, 'Dashboard/search.html', {'filter': user_filter})

def add_show_movie(request):
    queries = Movie.objects.all()
    return render(request, 'Dashboard/addshow_movie.html', {'movie_data': queries})


@api_view(['GET', 'POST'])
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def view_by_rating(request):
    """ filter Movie rating """
    print("ajax called")
    if is_ajax(request=request) or request.method == 'GET':
        rate = request.GET.get('rating')
        if rate:
            movies_by_rating = Movie.objects.filter(rating__startswith=rate)
            print("movie_rates", movies_by_rating)
            serializer = serial.MovieSerializer(movies_by_rating, many=True)
            return JsonResponse({"moviesByRating": serializer.data}, status=200)
    else:
        movies_by_rating = Movie.objects.all()
        serializer = serial.MovieSerializer(movies_by_rating, many=True)
        return JsonResponse({"movies_by_rating": serializer.data}, status=200)


@api_view(['GET', 'POST'])
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def view_by_release_date(request):
    """ filter Movie date """
    print("ajax called")
    if is_ajax(request=request) or request.method == 'GET':
        release_date = request.GET.get('release_date')
        movies_by_date = Movie.objects.filter(release_date__icontains=release_date)
        print("movie_rates", movies_by_date)
        serializer = serial.MovieSerializer(movies_by_date, many=True)
        return JsonResponse({"movies_by_date": serializer.data}, status=200)
    else:
        movies_by_date = Movie.objects.all()
        serializer = serial.MovieSerializer(movies_by_date, many=True)
        return JsonResponse({"movies_by_date": serializer.data}, status=200)


@api_view(['GET', 'POST'])
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def view_by_actors(request):
    """ filter Movie actor names """
    print("ajax called")
    if is_ajax(request=request) or request.method == 'GET':
        actors = request.GET.get('actors')
        actors = request.GET.get('actors')
        print("actors",actors)
        movies_by_actors = Movie.objects.filter(actors__name__icontains=actors)
        print("movie_rates", movies_by_actors)
        serializer = serial.MovieSerializer(movies_by_actors, many=True)
        return JsonResponse({"movies_by_actors": serializer.data}, status=200)
    else:
        movies_by_actors = Movie.objects.all()
        serializer = serial.MovieSerializer(movies_by_actors, many=True)
        return JsonResponse({"movies_by_actors": serializer.data}, status=200)


@api_view(['GET','POST'])
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def view_by_genres(request):
    """ filter Movie genre types """
    print("ajax called")
    if is_ajax(request=request) or request.method == 'GET':
        genres = request.GET.get('genres')
        print("genre",genres)

        movies_by_genres = Movie.objects.filter(genres__type__icontains=genres)
        print("movie_rates", movies_by_genres)

        serializer = serial.MovieSerializer(movies_by_genres, many=True)
        return JsonResponse({"movies_by_genres": serializer.data}, status=200)

    else:
        movies_by_genres = Movie.objects.all()
        serializer = serial.MovieSerializer(movies_by_genres, many=True)
        return JsonResponse({"movies_by_genres": serializer.data}, status=200)


def index(request):
    """ Search rating,movie name,movie dates,genre and actors  """
    if request.method == 'GET':
        search = request.GET.get('q')
        print("any value : ", search)

        if search:
            print("all search condition")
            all_search = Movie.objects.filter(name__icontains=search) or Movie.objects.filter(actors__name__icontains=search) or Movie.objects.filter(genres__type__icontains=search) or Movie.objects.filter(release_date__icontains=search) or Movie.objects.filter(rating__icontains=search)
            return render(request, 'Dashboard/filter_movie.html', {'movie_data': all_search})

        else:
            queries = Movie.objects.all()
            return render(request, 'Dashboard/filter_movie.html', {'movie_data': queries})
    else:
        print("else all search else condition")
        queries = Movie.objects.all()
        return render(request, 'Dashboard/filter_movie.html', {'movie_data': queries})



def filter_movie(request):
    """ showing filter of rating,movie name,movie dates,genre and actors  """
    queries = Actor.objects.all()
    genre = Genres.objects.all()
    return render(request, 'Dashboard/addshow_movie.html', {'actor_nm':queries,'genres':genre})


###################### Rest Framework Start Here   ###############################


class MovieCrud(ModelViewSet):
    """ Crud for Movie model  """
    queryset = Movie.objects.all()
    serializer_class = MovieApiSerializer
    pagination_class = StandardResultsSetPagination


class ActorCrud(ModelViewSet):
    """ Crud for Actor model  """
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    pagination_class = StandardResultsSetPagination


class GenresCrud(ModelViewSet):
    """ Crud for Genre model  """
    queryset = Genres.objects.all()
    serializer_class = GenresSerializer
    pagination_class = StandardResultsSetPagination


@api_view(['GET', 'POST'])
def view_by_rating_api(request):
    """ Api endpoint for movie rating  """
    print("ajax called")
    jsondata = request.data
    if jsondata:
        rates = jsondata.get('rating')
        movies_by_rating = Movie.objects.filter(rating__startswith=rates)
        print("movie_rates", movies_by_rating)
        serializer = serial.MovieApiSerializer(movies_by_rating, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return JsonResponse({"Failure": "Empty Body"})


@api_view(['GET', 'POST'])
def view_by_release_date_api(request):
    """ Api endpoint for release_date of movies  """
    print("ajax called")
    jsondata = request.data
    if jsondata:
        release_date = jsondata.get('release_date')
        movies_by_date = Movie.objects.filter(release_date__icontains=release_date)
        print("movie_rates", movies_by_date)
        serializer = serial.MovieApiSerializer(movies_by_date, many=True)
        return JsonResponse({"movies_by_date": serializer.data}, status=200)
    else:
        return JsonResponse({"Failure": "Empty Body"})


@api_view(['GET', 'POST'])
def view_by_actors_api(request):
    """ Api endpoint for actors of movies  """
    print("ajax called")
    jsondata = request.data
    if jsondata:
        actors = jsondata.get('actors')
        movies_by_actors = Movie.objects.filter(actors__name__icontains=actors)
        print("movie_rates", movies_by_actors)
        serializer = serial.MovieApiSerializer(movies_by_actors, many=True)
        return JsonResponse({"movies_by_actors": serializer.data}, status=200)
    else:
        return JsonResponse({"Failure": "Empty Body"})


@api_view(['GET', 'POST'])
def view_by_genres_api(request):
    """ Api endpoint for genre of movies  """
    print("ajax called")
    jsondata = request.data
    if jsondata:
        genres = jsondata.get('genres')
        movies_by_genres = Movie.objects.filter(genres__type__icontains=genres)
        print("movie_rates", movies_by_genres)
        serializer = serial.MovieApiSerializer(movies_by_genres, many=True)
        return JsonResponse({"movies_by_genres": serializer.data}, status=200)
    else:
        return JsonResponse({"Failure": "Empty Body"})


@api_view(['GET', 'POST'])
def search_by_all_api(request):
    """ Api endpoint for searching of all fields of models  """
    print("ajax called")
    jsondata = request.data
    if jsondata:
        if jsondata.get('name'):
            search = jsondata.get('name')
            print("search", search)
            query = Movie.objects.filter(name__icontains=search)
        if jsondata.get('rating'):
            search = jsondata.get('rating')
            print("search", search)
            query = Movie.objects.filter(rating__icontains=search)
        if jsondata.get('actors'):
            search = jsondata.get('actors')
            print("search", search)
            query = Movie.objects.filter(actors__name__icontains=search)
        if jsondata.get('release_date'):
            search = jsondata.get('release_date')
            print("search", search)
            query = Movie.objects.filter(release_date__icontains=search)
        if jsondata.get('genres'):
            search = jsondata.get('genres')
            print("search", search)
            query = Movie.objects.filter(genres__type__icontains=search)
        serializer = serial.MovieApiSerializer(query, many=True)
        return JsonResponse({"query": serializer.data}, status=200)
    else:
        return JsonResponse({"Failure": "Empty Body"})


