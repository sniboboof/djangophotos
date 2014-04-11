from django.db import models


class User(models.Model):
    name = models.CharField(max_length=128)
    pwdhash = models.CharField(max_length=128)
    email = models.CharField(max_length=128)

    def __unicode__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=128)

    def __unicode__(self):
        return self.name


class Photo(models.Model):
    filename = models.CharField(max_length=128)
    owner = models.ForeignKey(User)
    tags = models.ManyToManyField(Tag)

    def __unicode__(self):
        return self.filename


class Album(models.Model):
    name = models.CharField(max_length=128)
    owner = models.ForeignKey(User)
    photos = models.ManyToManyField(Photo)

    def __unicode__(self):
        return self.name
