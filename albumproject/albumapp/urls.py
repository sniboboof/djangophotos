from django.conf.urls import patterns, url


urlpatterns = patterns(
    'albumapp.views',

    url(r'^$',
        'front_view',
        name='frontpage'),

    url(r'^home/$',
        'home_view',
        name='homepage'),

    url(r'^home/album/(\d+)/$',
        'album_view',
        name='albumpage'),

    url(r'^home/photo/(\d+)/$',
        'photo_view',
        name='photopage'),

    url(r'^home/tag/(\d+)/$',
        'tag_view',
        name='tagpage'),
)