from django.db import models


class Bandname(models.Model):
    bandname_text = models.CharField(max_length=255)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.bandname_text

    def roll_dice(self):
        return self.count()
