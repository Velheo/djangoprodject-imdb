# Create your models here.
from django.db import models
from django.urls import reverse
import datetime


class Director(models.Model):
    last=models.CharField(max_length=20)
    first=models.CharField(max_length=20)
    bio=models.FileField(null=True, blank=True, upload_to='bio/')
    img=models.ImageField(null=True, blank=True, upload_to='directors/')
    def __str__(self):
        return self.first+' '+self.last

    def url(self):
        return reverse('imdb:director_detail', args=[self.id])

    def get_avg_rating(self):
       movies=Movie.objects.filter(director__id__exact=self.id)
       if not movies:
           return 0.0
       return sum(movie.rating for movie in movies)/len(movies)

    def get_avg_rating_str(self):
        return f'{self.get_avg_rating():.1f}'

    def get_best_movie(self):
        movies=Movie.objects.filter(director__id__exact=self.id)
        if len(movies) in (0,1):
            return None
        return max(movies,key=lambda m: m.rating)

    class Meta:
        ordering = ['last', 'first']

class Movie(models.Model):
    title=models.CharField(max_length=50)
    year=models.IntegerField(default=0)
    img=models.ImageField(null=True, blank=True, upload_to='movies/')
    plot=models.FileField(null=True, blank=True, upload_to='plots/')
    rating=models.FloatField(default=5.0)
    views = models.IntegerField(default=0)
    director=models.ForeignKey(Director, blank=True, null=True, on_delete=models.SET_NULL)
    trailer=models.FileField(null=True, blank=True, upload_to='trailer/')

    def __str__(self):
        return self.title

    def url(self):
        return reverse('imdb:movie_detail', args=[self.id])

    class Meta:
        ordering=['title']

class MovieComment(models.Model):
    text=models.CharField(max_length=1020)
    author= models.CharField(max_length=32)
    published=models.DateTimeField(default=datetime.datetime.now)
    movie=models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.text} Comment by {self.author} /{self.published}'

#class Actors