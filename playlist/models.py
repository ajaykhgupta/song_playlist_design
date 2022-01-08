from django.db import models

# Create your models here.
class songlist(models.Model):
    songname = models.CharField(max_length=60)
    artist = models.CharField(max_length=60)
    release_year = models.IntegerField(null=True)
    genre = models.TextField()

    def __str__(self):
        return self.songname