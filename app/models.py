from django.db import models
from django.urls import reverse
from django.conf import settings

class Category(models.Model):
    name = models.CharField(max_length=25)
    description = models.TextField()

    def __str__(self):
        return self.name

class Artwork(models.Model):
    artist = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, related_name='artworks')
    title = models.CharField(max_length=25)
    description = models.TextField()
    image = models.ImageField(upload_to='artworks/')
    date_uploaded = models.DateTimeField(auto_now_add=True, null=True, blank=True,)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='artworks')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('artwork_detail', kwargs={'pk': self.pk})



class Exhibition(models.Model):
    title = models.CharField(max_length=30)
    date = models.DateField()
    location = models.CharField(max_length=200)
    artworks = models.ManyToManyField(
        Artwork,
        related_name='exhibitions'
    )
    artist = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name='created_exhibitions'
    )


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('exhibition_detail', kwargs={'pk': self.pk})




class Comment(models.Model):
    artwork = models.ForeignKey(Artwork,related_name='comments', on_delete=models.CASCADE  )
    user = models.ForeignKey( settings.AUTH_USER_MODEL,related_name='comments', on_delete=models.CASCADE, null=True, blank=True )
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.artwork.title

    def get_absolute_url(self):
        return reverse('artwork_detail', kwargs={'pk': self.pk})