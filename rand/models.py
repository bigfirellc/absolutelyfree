from django.db import models
from django.utils import timezone

# Create your models here.
class Bandname(models.Model):
    bandname_text = models.CharField(max_length=255)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.bandname_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def roll_dice(self):
        return self.count()

class Album(models.Model):
    name = models.CharField(max_length=1024)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.bandname_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def roll_dice(self):
        return self.count()      