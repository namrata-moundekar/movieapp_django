from rest_framework.serializers import ModelSerializer
from movie_app.models import Movie, Actor, Genres
from rest_framework import serializers


class GenresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genres
        fields = '__all__'


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    genres = GenresSerializer(many=True)
    actors = ActorSerializer(many=True)

    class Meta:
        model = Movie
        fields = '__all__'


class MovieApiSerializer(serializers.ModelSerializer):
    actors = serializers.StringRelatedField(many=True)
    genres = serializers.StringRelatedField(many=True)

    class Meta:
        model = Movie
        fields = '__all__'

