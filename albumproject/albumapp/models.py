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
    owner = models.ForeignKey(User)
    tags = models.ManyToManyField(Tag)
    height = models.IntegerField(blank=True, null=True, default=0)
    width = models.IntegerField(blank=True, null=True, default=0)
    image = models.ImageField(
        upload_to='%Y/%m/%d',
        height_field='height',
        width_field='width',
        )

    def __unicode__(self):
        return unicode(self.pk)


class Album(models.Model):
    name = models.CharField(max_length=128)
    owner = models.ForeignKey(User)
    photos = models.ManyToManyField(Photo)

    def __unicode__(self):
        return self.name
