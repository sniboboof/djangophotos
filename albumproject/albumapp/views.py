from django.shortcuts import render, redirect


def front_view(request):
    return render(request, 'front.html')


def home_view(request):
    return render(request, 'home.html')


def album_view(request, albumid):
    myalbum = Album.objects.get(pk=albumid)
    return render(request, 'album.html', {'photos': myalbum.photos.all()})


def photo_view(request, photoid):
    myphoto = Photo.objects.get(pk=photoid)
    return render(request, 'photo.html', {'photo': myphoto})


def tag_view(request, tagid):
    mytag = Tag.objects.get(pk=tagid)
    return render(request, 'tag.html', {'photos': mytag.photos.all()})
