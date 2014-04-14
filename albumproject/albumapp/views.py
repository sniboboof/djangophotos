from django.shortcuts import render, redirect
from models import User, Photo, Album, Tag


def front_view(request):
    return render(request, 'front.html')


def home_view(request):
    return render(request, 'home.html', {'albums': Album.objects.all()})


def album_view(request, albumid):
    myalbum = Album.objects.get(pk=albumid)
    return render(request, 'album.html', {'photos': myalbum.photos.all()})


def photo_view(request, photoid):
    myphoto = Photo.objects.get(pk=photoid)
    return render(request, 'photo.html', {'photo': myphoto})


def tag_view(request, tagid):
    mytag = Tag.objects.get(pk=tagid)
    taggedphotos = Photo.objects.filter(tags=mytag).all()
    return render(request, 'tag.html', {'photos': taggedphotos, 'tag': mytag})
