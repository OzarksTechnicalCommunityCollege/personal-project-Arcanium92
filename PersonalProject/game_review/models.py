from django.conf import settings
from django.db import models
from django.db.models.functions import Now

# Create your models here.
class GameReview(models.Model):
    title = models.CharField(max_length=250)
    reviewer = models.CharField(max_length=250)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='game_reviews', null=True, blank=True)
    rating = models.IntegerField()
    review_text = models.TextField()
    submission = models.DateTimeField(db_default=Now())
    created = models.DateTimeField(auto_now_add=True) #Stores date and time post was created
    updated = models.DateTimeField(auto_now_add=True) #Stores time and date post was updated

    class Meta:
        ordering = ['-created'] #Meta class for sort order
        indexes = [
            models.Index(fields=['-created']),
        ] #Database index

    def __str__(self):
        return f"{self.title} | {self.reviewer} | {self.rating}"


#Create user profile model
class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(
        upload_to='users/%y/%m/%d',
        blank=True
    )
    def __str__(self):
        return f'Profile of {self.user.username}'