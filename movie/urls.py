"""Milestone_Trackers URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from movie_app import views
from django.conf.urls.static import static
from django.conf import settings
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Movie Showbox')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('filter/', views.index, name='filter'),
    path('filter_movie/', views.filter_movie, name='filter_movie'),
    path('filter_movie/rating_search', views.view_by_rating, name='filter/rating_search'),
    path('filter_movie/date_search', views.view_by_release_date, name='filter/date_search'),
    path('filter_movie/actor_search', views.view_by_actors, name='filter/actor_search'),
    path('filter_movie/genres_search', views.view_by_genres, name='filter/genres_search'),
    path('filter_movie/rating_api', views.view_by_rating_api, name='api_rating'),
    path('filter_movie/date_api', views.view_by_release_date_api, name='api_date'),
    path('filter_movie/actor_api', views.view_by_actors_api, name='api_actor'),
    path('filter_movie/genres_api', views.view_by_genres_api, name='api_genres'),
    path('filter_movie/search_api', views.search_by_all_api, name='api_search'),
    path('swagger/', schema_view),
    path('movie_showbox/',include('movie_app.urls')),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



