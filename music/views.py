from django.http import Http404
from django.shortcuts import render
from .models import Album

def index(request):
    albums = Album.objects.all()
    context = {'albums':albums}
    return render(request, 'music/index.html', context)

def name(request, number):
    try:
        album = Album.objects.get(id=number)
    except Album.DoesNotExist:
        raise Http404("Album does not exist")
    context = {'album':album}
    return render(request, 'music/name.html', context)