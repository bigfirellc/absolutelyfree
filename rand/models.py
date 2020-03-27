from django.db import models
from django.utils import timezone

# Create your models here.
class Bandname(models.Model):
    bandname_text = models.CharField(max_length=255, verbose_name="Band Name")
    pub_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.bandname_text


class Album(models.Model):
    album_text = models.CharField(max_length=1024, verbose_name="Album Title")
    pub_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.album_text        