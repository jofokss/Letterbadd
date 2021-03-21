from django.shortcuts import render, redirect
from badboxd.models import FavoriteMovies
from badboxd.forms import FMoviesForms


# Create your views here.
def emp(request):
    if request.method == "POST":
        form = FMoviesForms(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show/')
            except:
                pass
    else:
        form = FMoviesForms()
    return render(request, 'index.html', {'form': form})


def show(request):
    fmovies=FavoriteMovies.objects.all()
    return render(request, "show.html", {'fmovies': fmovies})


def edit(request, id):
    fmovie = FavoriteMovies.objects.get(id=id)
    return render(request, 'edit.html', {'fmovie': fmovie})


def update(request, id):
    fmovie = FavoriteMovies.objects.get(id=id)
    form = FMoviesForms(request.POST, instance=fmovie)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request, 'edit.html', {'fmovie': fmovie})


def destroy(request, id):
    fmovie = FavoriteMovies.objects.get(id=id)
    fmovie.delete()
    return redirect("/show")
