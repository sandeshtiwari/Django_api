from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=32)
    description = models.CharField(max_length=300)

    def avg_rating(self):
        sum = 0
        all_ratings = Rating.objects.filter(movie=self)
        for rating in all_ratings:
            sum += rating.stars
        if len(all_ratings) > 0:
            return (sum/len(all_ratings))
        else:
            return 0

    def num_of_rating(self):
        all_ratings = Rating.objects.filter(movie=self)
        return len(all_ratings)

class Rating(models.Model):
    stars = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        unique_together = (('user','movie'),)
        index_together = (('user','movie'),)
