from django.test import TestCase
import models


class AlbumAppModelTestCase(TestCase):

    def testUser(self):
        models.User.objects.create(name='jack',
                                   pwdhash='fiddlefaddle',
                                   email='jim@darkmagic.com')
        models.User.objects.create(name='ben',
                                   pwdhash='biddlebaddle',
                                   email='bim@darkmagic.com')
        models.User.objects.create(name='ann',
                                   pwdhash='aiddleaaddle',
                                   email='aim@darkmagic.com')
        self.assertEqual(models.User.objects.get(name='jack').pwdhash,
                         'fiddlefaddle')
        self.assertEqual(models.User.objects.get(name='ben').email,
                         'bim@darkmagic.com')
        self.assertEqual(models.User.objects.get(name='ann').pwdhash,
                         'aiddleaaddle')

    def testPhoto(self):
        models.User.objects.create(name='jack',
                                   pwdhash='fiddlefaddle',
                                   email='jim@darkmagic.com')
        models.User.objects.create(name='ben',
                                   pwdhash='biddlebaddle',
                                   email='bim@darkmagic.com')
        models.User.objects.create(name='ann',
                                   pwdhash='aiddleaaddle',
                                   email='aim@darkmagic.com')

        tempowner = models.User.objects.get(name='jack')
        models.Photo.objects.create(filename='busy.jpg',
                                    owner=tempowner)
        models.Photo.objects.create(filename='adventure.gif',
                                    owner=tempowner)

        tempowner = models.User.objects.get(name='ben')
        models.Photo.objects.create(filename='soup.gif',
                                    owner=tempowner)

        tempowner = models.User.objects.get(name='ann')
        models.Photo.objects.create(filename='car.png',
                                    owner=tempowner)

        tempphoto = models.Photo.objects.get(filename='busy.jpg')
        self.assertEqual(tempphoto.filename, 'busy.jpg')
        self.assertEqual(tempphoto.owner, models.User.objects.get(name='jack'))
        tempphoto = models.Photo.objects.get(filename='adventure.gif')
        self.assertEqual(tempphoto.filename, 'adventure.gif')
        self.assertEqual(tempphoto.owner, models.User.objects.get(name='jack'))

        tempphoto = models.Photo.objects.get(filename='soup.gif')
        self.assertEqual(tempphoto.filename, 'soup.gif')
        self.assertEqual(tempphoto.owner, models.User.objects.get(name='ben'))

        tempphoto = models.Photo.objects.get(filename='car.png')
        self.assertEqual(tempphoto.filename, 'car.png')
        self.assertEqual(tempphoto.owner, models.User.objects.get(name='ann'))

    def testAlbum(self):
        tempowner = models.User.objects.create(name='jack',
                                               pwdhash='fiddlefaddle',
                                               email='jim@darkmagic.com')
        models.Photo.objects.create(filename='busy.jpg',
                                    owner=tempowner)
        tempowner = models.User.objects.create(name='ben',
                                               pwdhash='biddlebaddle',
                                               email='bim@darkmagic.com')
        models.Photo.objects.create(filename='soup.gif',
                                    owner=tempowner)
        tempowner = models.User.objects.create(name='ann',
                                               pwdhash='aiddleaaddle',
                                               email='aim@darkmagic.com')
        models.Photo.objects.create(filename='car.png',
                                    owner=tempowner)

        tempowner = models.User.objects.get(name='jack')
        tempalbum = models.Album.objects.create(name='school',
                                                owner=tempowner)
        tempphoto = models.Photo.objects.get(filename='busy.jpg')
        tempalbum.photos.add(tempphoto)
        tempphoto = models.Photo.objects.get(filename='soup.gif')
        tempalbum.photos.add(tempphoto)

        tempowner = models.User.objects.get(name='ben')
        tempalbum = models.Album.objects.create(name='work',
                                                owner=tempowner)
        tempphoto = models.Photo.objects.get(filename='soup.gif')
        tempalbum.photos.add(tempphoto)
        tempphoto = models.Photo.objects.get(filename='car.png')
        tempalbum.photos.add(tempphoto)

        tempuser = models.User.objects.get(name='jack')
        tempalbum = models.Album.objects.get(name='school')
        tempphoto = tempalbum.photos.get(filename='busy.jpg')
        expectedphoto = models.Photo.objects.get(filename='busy.jpg')
        self.assertEqual(tempphoto, expectedphoto)
        tempphoto = tempalbum.photos.get(filename='soup.gif')
        expectedphoto = models.Photo.objects.get(filename='soup.gif')
        self.assertEqual(tempphoto, expectedphoto)

        tempalbum = models.Album.objects.get(name='work')
        tempphoto = tempalbum.photos.get(filename='soup.gif')
        expectedphoto = models.Photo.objects.get(filename='soup.gif')
        self.assertEqual(tempphoto, expectedphoto)
        tempphoto = tempalbum.photos.get(filename='car.png')
        expectedphoto = models.Photo.objects.get(filename='car.png')
        self.assertEqual(tempphoto, expectedphoto)

    def testTag(self):
        tempowner = models.User.objects.create(name='jack',
                                               pwdhash='fiddlefaddle',
                                               email='jim@darkmagic.com')
        models.Photo.objects.create(filename='busy.jpg',
                                    owner=tempowner)
        tempowner = models.User.objects.create(name='ben',
                                               pwdhash='biddlebaddle',
                                               email='bim@darkmagic.com')
        models.Photo.objects.create(filename='soup.gif',
                                    owner=tempowner)
        tempowner = models.User.objects.create(name='ann',
                                               pwdhash='aiddleaaddle',
                                               email='aim@darkmagic.com')
        models.Photo.objects.create(filename='car.png',
                                    owner=tempowner)

        tempphoto = models.Photo.objects.get(filename='busy.jpg')
        temptag = models.Tag.objects.create(name='testtag')
        tempphoto.tags.add(temptag)
        expectedtag = tempphoto.tags.get(name='testtag')
        self.assertEqual(temptag, expectedtag)

    def testUnicode(self):
        tempowner = models.User.objects.create(name='jack',
                                               pwdhash='fiddlefaddle',
                                               email='jim@darkmagic.com')
        self.assertEqual(tempowner.name, str(tempowner))
        tempphoto = models.Photo.objects.create(filename='busy.jpg',
                                                owner=tempowner)
        self.assertEqual(tempphoto.filename, str(tempphoto))
        temptag = models.Tag.objects.create(name='testtag')
        self.assertEqual(temptag.name, str(temptag))
        tempalbum = models.Album.objects.create(name='testalbum',
                                                owner=tempowner)
        self.assertEqual(tempalbum.name, str(tempalbum))
