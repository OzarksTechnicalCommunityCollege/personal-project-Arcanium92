from django.shortcuts import render, redirect
from .models import GameReview
from .forms import GameReviewForm

# Create your views here.
def review_list(request):
    reviews = GameReview.objects.all()
    return render(request, "game_review/review_list.html", {"reviews": reviews})

def add_review(request):
    if request.method == "POST":
        form = GameReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('review_list')
    else:
        form = GameReviewForm()
    return render(request, "game_review/add_review.html", {"form": form})
