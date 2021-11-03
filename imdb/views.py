from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.http import HttpResponseRedirect
from django.db.models import Q

from rest_framework import generics

from .models import *
from .serializers import *
from .forms import *
# Create your views here.
class IndexView(ListView):
    template_name = 'imdb/index.html'
    context_object_name = 'last_movies'

    def get_queryset(self):
        return Movie.objects.order_by('-id')[:4]

    def get_context_data(self,  **kwargs):
        context=super().get_context_data()
        context['best_movie_list']=Movie.objects.order_by('-rating')[:4]
        context['best_directors'] = sorted(Director.objects.all(), key=lambda d: -d.get_avg_rating())[:4]
#        context['popular_movies'] = Movie.object.order.by('-views')[:4]
        return context


class MovieListView(ListView):
    model = Movie
    context_object_name = 'movies'

#class MovieDetailView(DetailView):
#    model = Movie
#    def get_object(self, queryset=None):
#        obj=super().get_object()
 #       obj.views +=1
 #       obj.save()
 #       return obj
def movie_detail(request, pk):
    model = Movie
    movie = Movie.objects.get(pk=pk)
    movie.views += 1
    movie.save()
    context = {
        'movie': movie,
    }
    return render(request, 'imdb/movie_detail.html', context)

class BestMovieListView(ListView):
    template_name = 'imdb/best_movie_list.html'
    context_object_name = 'movies'
    def get_queryset(self):
        return Movie.objects.order_by('-rating')

class DirectorListView(ListView):
    model = Director
    context_object_name = 'directors'

class DirectorDetailView(DetailView):
    model = Director


def search(request):
    string=request.POST.get('search')
    if string:
        context={
            'string': string,
            'movies': Movie.objects.filter(title__icontains=string),
            'directors': Director.objects.filter(Q(last__icontains=string)|Q(first__icontains=string)),
        }
        return render(request, 'imdb/search.html', context)
    else:
        return HttpResponseRedirect(reverse('imdb:index'))

#API
class MovieListAPIView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer1

def config(request):
    context={
        'movie_form': MovieModelForm()
    }
    return render(request, 'imdb/config.html', context)

def add_movie(request):
    form=MovieModelForm(request.POST)
    saved=form.save(commit=False)
    saved.img=request.FILES['img']
    saved.plot=request.FILES['plot']
    saved.trailer=request.FILES['trailer']
    saved.save()
    return HttpResponseRedirect(reverse('imdb:movie_list'))

#def add_director(request):
#    form=DirectorModelForm(request.POST)
#    saved=form.save(commit=False)
#    saved.img=request.FILES['img']
#    saved.bio = request.FILES['bio']
#    saved.save()
#    return HttpResponseRedirect(reverse('imdb:director_list'))

#def add_comment(request, pk):
    #text = request.form.get('text')
    #author = request.form.get('author')
   # email = request.form.get('email')
  #  if author and text and email:

 #   return render()
#class MovieListAPIView(generics.ListAPIView):
#    queryset = Movie.objects.all()
#    serializer_class = MovieSerializer2
