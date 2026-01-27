from django import forms
from .models import GameReview

# form using django default form
class GameReviewForm(forms.ModelForm):
    class Meta:
        model = GameReview
        fields = ['title', 'reviewer', 'rating', 'review_text']