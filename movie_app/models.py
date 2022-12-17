from django.db import models


# Create your models here.

class Director(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField()
    duration = models.DurationField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Review(models.Model):
    text = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id}_{self.movie}"
