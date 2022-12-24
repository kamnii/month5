from django.db import models


# Create your models here.

class Director(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField()
    duration = models.IntegerField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE,
                                 related_name='movie')

    def __str__(self):
        return self.title


class Review(models.Model):
    text = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE,
                              related_name='reviews')

    stars = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5')
    )

    grade = models.IntegerField(default=1, choices=stars)

    def __str__(self):
        return f"{self.id}_{self.movie}"
