from django.db import models
from django.db.models.functions import Now

# Create your models here.
class GameReview(models.Model):
    title = models.CharField(max_length=250)
    reviewer = models.CharField(max_length=250)
    rating = models.IntegerField()
    review_text = models.TextField()
    submission = models.DateTimeField(db_default=Now())
    created = models.DateTimeField(auto_now_add=True) #Stores date and time post was created
    updated = models.DateTimeField(auto_now_add=True) #Stores time and date post was updated

    class Meta:
        ordering = ['-review_text'] #Meta class for sort order
        indexes = [
            models.Index(fields=['-review_text']),
        ] # Database index

    def __str__(self):
        return self.title, self.reviewer, self.rating, self.review_text, self.submission