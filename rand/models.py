from django.db import models
from import_export import resources


class Bandname(models.Model):
    bandname_text = models.CharField(max_length=255, verbose_name="Band Name")
    openai_prompt = models.TextField(
        null=True, blank=True, verbose_name="OpenAI Prompt"
    )
    image = models.ImageField(null=True, blank=True, upload_to="img/")
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.bandname_text

    def roll_dice(self):
        return self.count()


class Album(models.Model):
    name = models.CharField(max_length=1024, verbose_name="Album Name")
    openai_prompt = models.TextField(
        null=True, blank=True, verbose_name="OpenAI Prompt"
    )
    image = models.ImageField(null=True, blank=True, upload_to="img/")
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def roll_dice(self):
        return self.count()


class AlbumResource(resources.ModelResource):
    class Meta:
        model = Album
        import_id_fields = ("id",)
        fields = ("id", "name", "openai_prompt", "pub_date")


class BandnameResource(resources.ModelResource):
    class Meta:
        model = Bandname
        import_id_fields = ("id",)
        fields = ("id", "bandname_text", "openai_prompt", "pub_date")
