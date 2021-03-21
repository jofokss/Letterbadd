from django.forms import ModelForm
from badboxd.models import FavoriteMovies



class FMoviesForms(ModelForm):
    class Meta:
        model = FavoriteMovies
        fields = ['name', 'watchedDate', 'rating']
