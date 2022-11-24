from django.db import models
# from multiselectfield import MultiSelectField
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Genres(models.Model):
    type = models.CharField(max_length=60,null=True,blank=True,unique=True)

    class meta:
        db_table ='GENRES_INFO'

    def __str__(self):
        return self.type

class Actor(models.Model):
    name= models.CharField(max_length=60,null=True,blank=True)
    age = models.IntegerField()

    class Meta:
        db_table = 'ACTOR_INFO'

    def __str__(self):
        return self.name


class Movie(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    release_date = models.DateField(null=True,blank=True)
    poster_image = models.ImageField(upload_to='images/',max_length=1000,null=True,blank=True)
    rating = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(10.0)])
    genres = models.ManyToManyField(Genres,related_name='movie_genres')
    actors = models.ManyToManyField(Actor,related_name='movie_actor')

    class Meta:
        db_table = 'MOVIE_INFO'

    def __str__(self):
        return self.name





        

