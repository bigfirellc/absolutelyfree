from django.db import models


class Bandname(models.Model):
    bandname_text = models.CharField(max_length=255, verbose_name="Band Name")
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.bandname_text.title()

    def roll_dice(self):
        return self.count()


class Album(models.Model):
    name = models.CharField(max_length=1024, verbose_name="Album Name")
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name.title()

    def roll_dice(self):
        return self.count()
