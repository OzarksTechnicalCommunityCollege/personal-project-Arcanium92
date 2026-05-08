from django.db import models

class ReviewScore(models.Model):
    gameName = models.CharField(max_length=50)
    rating = models.IntegerField()

    def __str__(self):
        return f"{self.gameName}: {self.rating}"