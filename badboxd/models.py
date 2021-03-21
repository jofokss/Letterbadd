from django.db import models


# Create your models here.

RatingChoices = [
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (4, 4),
    (5, 5),
    (6, 6),
    (7, 7),
    (8, 8),
    (9, 9),
    (10, 10),

]

class FavoriteMovies(models.Model):
    name = models.CharField(max_length=168, blank=True, null=True)
    watchedDate = models.DateField()
    rating = models.IntegerField(blank=True, null= True, choices= RatingChoices)

    class Meta:
        db_table = "FMovies"