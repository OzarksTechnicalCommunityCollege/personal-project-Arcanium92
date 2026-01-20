from django.shortcuts import render
from .models import GameReview

# Create your views here.
def review_list(request):
    reviews = GameReview.objects.all()
    return render(request, "game_review/review_list.html", {"reviews": reviews})